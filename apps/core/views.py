from django.shortcuts import render, redirect
from apps.event.models import Category, Event
from apps.core.forms import SignupForm
from django.contrib.auth import logout


def index(request):
    events = Event.objects.filter(is_sold=False)[0:8]
    categories = Category.objects.all()
    return render(
        request, "core/index.html", {"categories": categories, "items": events}
    )


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:

        form = SignupForm()

    return render(request, "core/signup.html", {"form": form})


def about_us(request):
    return render(request, "core/about.html")


def terms_of_service(request):
    return render(request, "core/terms.html")


def privacy_policy(request):
    return render(request, "core/privacy.html")


def logout_view(request):
    logout(request)
    return redirect("/")
