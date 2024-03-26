from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@n-pjgx7&8@a$q*#!47u7un9eghexs4z*!&&e+3(vbys%s2q35"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.core",
    "apps.event",
    "apps.dashboard",
    "django_daraja",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
SESSION_COOKIE_AGE = 600  # 10 minutes - Log out user after inactivity in 5 minutes

ROOT_URLCONF = "eticket.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "eticket.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MPESA_ENVIRONMENT = "sandbox"

# Credentials for the daraja app

MPESA_CONSUMER_KEY = "nk16Y74eSbTaGQgc9WF8j6FigApqOMWr"
MPESA_CONSUMER_SECRET = "40fD1vRXCq90XFaU"

# Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

MPESA_SHORTCODE = "174379"

# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This is only used on sandbox, do not set this variable in production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

MPESA_EXPRESS_SHORTCODE = "174379"

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

MPESA_SHORTCODE_TYPE = "paybill"

# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = "testapi"

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_SECURITY_CREDENTIAL = "Safaricom999!*!"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
         'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '{asctime} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'daraja.log'),
            'formatter': 'simple',
            'maxBytes': 1024*1024*15, # 15MB
            'backupCount': 10,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'daraja': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
