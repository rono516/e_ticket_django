from django.contrib import admin
from .models import Category
from .models import Event


admin.site.register(Category)
admin.site.register(Event)
