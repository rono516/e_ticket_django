from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "item"
urlpatterns = [
    path("", views.items, name="items"),
    path("new/", views.new, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path("<int:pk>/edit", views.edit, name="edit"),
    path("stk_push", views.stk_push, name="stk_push"),
    path("daraja/stk_push", views.stk_push_callback, name="stk_push_callback"),
    # path("mpesa_access_token", views.getAccessToken, name="mpesa_access_token"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
