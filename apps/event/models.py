from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    category = models.ForeignKey(
        Category, related_name="events", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="event_images", null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} in {self.category}"


class MpesaResponseBody(AbstractBaseModel):
    body = models.JSONField()
