from django import forms
from .models import Event

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            "category",
            "title",
            "description",
            "price",
            "image",
        )

        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASSES}),
            "title": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            "title",
            "description",
            "price",
            "image",
            "is_sold",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
