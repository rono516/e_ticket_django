from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import NewItemForm, UpdateItemForm
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
import logging

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
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0792009556'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://1e78-197-231-183-90.ngrok-free.app/api/mpesa/callback'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    print(response.content)
    return HttpResponse(response)
# @login_required
# def stk_push_callback(request):
#         data = request.body

#         print(data)

#         return HttpResponse("STK Push in Django👋")
@login_required
def stk_push_callback(request):
    try:
        # Read the callback data
        data = request.body.decode('utf-8')
        logging.info(f"Received M-Pesa callback data: {data}")

        # Process the callback data (e.g., update transaction status, log details, etc.)
        # ...

        return HttpResponse("STK Push in Django 👋")
    except Exception as e:
        logging.error(f"Error processing M-Pesa callback: {str(e)}")
        return HttpResponse(status=500)
