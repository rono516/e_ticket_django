from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'MPESA_CONFIG', None)

DEFAULTS = {
    'CONSUMER_KEY': "nk16Y74eSbTaGQgc9WF8j6FigApqOMWr",
    'CONSUMER_SECRET': "40fD1vRXCq90XFaU",
    'CERTIFICATE_FILE': None,
    'HOST_NAME': None,
    'PASS_KEY': "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
    'SAFARICOM_API': 'https://sandbox.safaricom.co.ke',
    'AUTH_URL': '/oauth/v1/generate?grant_type=client_credentials',
    'SHORT_CODE': "174379",
    'TILL_NUMBER': None,
    'TRANSACTION_TYPE': 'CustomerBuyGoodsOnline',
}

"""
CONSUMER_KEY="nk16Y74eSbTaGQgc9WF8j6FigApqOMWr"
CONSUMER_SECRET="40fD1vRXCq90XFaU"

{
    "phone_number": "2547920096556",
    "amount": 1,
    "entity_id": 1,
    "paybill_account_number": "174379"
}

"""

api_settings = APISettings(USER_SETTINGS, DEFAULTS, None)
