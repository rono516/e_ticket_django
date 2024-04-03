from rest_framework import serializers
from .models import MpesaResponseBody


class MpesaResponseBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaResponseBody
        fields = "__all__"
