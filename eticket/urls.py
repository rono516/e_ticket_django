from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mpesa.urls import mpesa_urls

urlpatterns = [
    path("", include("apps.core.urls"), name="index"),
    path("items/", include("apps.event.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("admin/", admin.site.urls),
    path("mpesa/", include(mpesa_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
