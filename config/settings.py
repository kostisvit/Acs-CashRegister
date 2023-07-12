import os
import sys
from pathlib import Path
import environ

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Initialise environment variables
from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

env = environ.Env()
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'tameiaki',
    'encrypted_model_fields',
    'import_export',
    'rest_framework',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_filters',
    'widget_tweaks',
    'captcha',
]

AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'tameiaki.context_processor.cash_count',
                'tameiaki.context_processor.cash_count_online',
                'tameiaki.context_processor.cash_count_offline',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Production
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.getenv('DATABASE_NAME'),
#         'USER': os.getenv('DATABASE_USER'),
#         'PASSWORD': os.getenv('DATABASE_PASS'),
#         'HOST': 'db',
#         'PORT': os.getenv('DATABASE_PORT'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

FIELD_ENCRYPTION_KEY = os.getenv('FIELD_ENCRYPTION_KEY')

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"


# Captcha settings
CAPTCHA_LENGTH = 5  # Number of characters in the captcha
CAPTCHA_FONT_SIZE = 30

# Add captcha field to authentication form
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

#AES_KEY_ENCRYPTION_KEY

FIELD_ENCRYPTION_KEY = env.str("FIELD_ENCRYPTION_KEY")


# Logging
# PATH = 'logs'
# if not os.path.exists(PATH):
#     os.makedirs(PATH)

# LOGGING = {
#     # Define the logging version
#     'version': 1,
#     # Enable the existing loggers
#     'disable_existing_loggers': False,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} [{name}:{lineno}] {message}",  # other options: {module} {process:d} {thread:d}
#             "datefmt": "%Y-%m-%d_%H:%M:%S",
#             "style": "{",
#         },
#         "simple": {
#             "format": "{levelname} {message}",
#             "style": "{",
#         },
#     },
#     # Define the handlers
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             "class": "logging.handlers.TimedRotatingFileHandler",
#             "formatter": "verbose",
#             # 'class': 'logging.FileHandler',
#             'filename': 'logs/server.log',
#             "when": "midnight",
#         },

#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },

#    # Define the loggers
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': True,

#         },
#     },
# }


LOG_ROOT = os.path.join(BASE_DIR, 'logs')

# Create a log directory if it doesn't exist
if not os.path.exists(LOG_ROOT):
    os.makedirs(LOG_ROOT)

# Function to generate the log file name based on the date
def get_log_file_path():
    now = datetime.now()
    log_dir = os.path.join(LOG_ROOT, now.strftime('%Y-%m'))
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return os.path.join(log_dir, now.strftime('%Y-%m-%d.log'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} [{name}:{lineno}] {message}",
            "datefmt": "%Y-%m-%d_%H:%M:%S",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': get_log_file_path(),
            "formatter": "verbose",
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}