from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, MpesaResponseBody
from .forms import NewItemForm, UpdateItemForm
from django.http import HttpResponse
import logging
from mpesa import LipaNaMpesaOnline
import os
# Set up logging
logging.basicConfig(filename='daraja.log', level=logging.INFO)

def items(request):
    query = request.GET.get("query", "")
    items = Event.objects.filter(is_sold=False)

    if query:
        items = items.filter(title__icontains=query)

    return render(
        request,
        "item/items.html",
        {
            "items": items,
            "query": query,
        },
    )


def detail(request, pk):
    item = get_object_or_404(Event, id=pk)
    related_items = Event.objects.filter(category=item.category, is_sold=False).exclude(
        id=pk
    )[0:3]

    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()

            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()

    return render(request, "item/form.html", {"form": form, "title": "New Item"})


@login_required
def edit(request, pk):
    item = get_object_or_404(Event, id=pk, added_by=request.user)
    if request.method == "POST":
        form = UpdateItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect("item:detail", pk=item.id)
    else:
        form = UpdateItemForm(instance=item)

    return render(request, "item/form.html", {"form": form, "title": "Update Item"})


@login_required
def delete(request, pk):
    item = get_object_or_404(Event, id=pk, added_by=request.user)
    item.delete()

    return redirect("dashboard:index")

@login_required
def stk_push(request):
    response = LipaNaMpesaOnline.sendSTK(amount=1, phone_number="254792009556",orderId=0,transaction_id=None,shortcode=174379,account_number=None)

    return HttpResponse(response)

# def stk_push_callback(request):
#     try:
#         # Read the callback data
#         data = request.body.decode('utf-8')
#         logging.info(f"Received M-Pesa callback data: {data}")

#         # Process the callback data (e.g., update transaction status, log details, etc.)
#         # ...

#         return HttpResponse("STK Push in Django 👋")
#     except Exception as e:
#         logging.error(f"Error processing M-Pesa callback: {str(e)}")
#         return HttpResponse(status=500)

def stk_push_callback(request):
    body = request.data
    if body:
        mpesa = MpesaResponseBody.objects.create(body=body)
        mpesa_body =mpesa.body

        current_directory = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_directory, 'mpesa_body.txt')

        # Write the mpesa_body to the text file
        with open(file_path, 'w') as file:
            file.write(str(mpesa_body))

        # if mpesa_body['stkCallback']['ResultCode'] == 0:
        #         transaction = Transaction.objects.create(
        #             phonenumber=mpesa_body['Body']['stkCallback']['CallbackMetadata']['Item'][-1]["Value"],
        #             amount=mpesa_body['Body']['stkCallback']['CallbackMetadata']['Item'][0]["Value"],
        #             receipt_no=mpesa_body['Body']['stkCallback']['CallbackMetadata']['Item'][1]["Value"]
        #         )

        #     return response.Response({"message": "Callback Data received and processed successfully."})
        # return response.Response({"failed": "No Callback Data Received"}, status=status.HTTP_400_BAD_REQUEST)

import requests
from requests.auth import HTTPBasicAuth
import json
request = ""
def getAccessToken(self):
    consumer_key = "nk16Y74eSbTaGQgc9WF8j6FigApqOMWr"
    consumer_secret = "40fD1vRXCq90XFaU"
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r= requests.get(api_url,auth=HTTPBasicAuth(consumer_key,consumer_secret))

    if r.status_code == 200:

        mpesa_access_token = json.loads(r.text)
        validated_access_token =mpesa_access_token['access_token']
        return validated_access_token
    elif r.status_code == 400:
        print("Invalid credentials")
        return False

