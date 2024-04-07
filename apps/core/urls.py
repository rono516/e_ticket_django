from django.urls import path
from apps.core import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib.auth import logout
app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path("about_us/", views.about_us, name="about_us"),
    path("terms_of_service/", views.terms_of_service, name="terms"),
    path("privacy_policy/", views.privacy_policy, name="privacy"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
    path("logout/", views.logout_view, name="logout"),

]
