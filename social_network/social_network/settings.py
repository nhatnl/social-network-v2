"""
Django settings for social_network project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6h9dj0*=xkcec6m1-bj+lw!sz%5!mgd))prwhq^v-$3fuc#p*#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'authentication',
    'custom_user',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_framework',
    'rest_framework.authtoken',
    'post',
    'comment',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_network.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_network.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default':{
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'social_network',
            'USER': 'postgres',
            'PASSWORD': '11',
            'HOST': 'localhost',
            'PORT': '5432',
        }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
    {
        'NAME': 'authentication.validator.PasswordValidation',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = { 
                "DEFAULT_PERMISSION_CLASSES": (
                                        "rest_framework.permissions.IsAuthenticated", 
                                        ),
                'DEFAULT_AUTHENTICATION_CLASSES': [
                                        'rest_framework.authentication.TokenAuthentication', 
                                        ],
                'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
                'PAGE_SIZE': 100,
                
                }
                            

AUTH_USER_MODEL = 'custom_user.CustomUser'

SITE_ID = 1

EMAIL_RESET_PASSWORD_EXPIRE_TIME = 10 #minutes


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_HMAC = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_AUTH_SERIALIZERS = {
                        'LOGIN_SERIALIZER': 'authentication.api.serializer.CustomLoginSerializer',
                        'PASSWORD_RESET_CONFIRM_SERIALIZER': 'authentication.api.serializer.CustomPasswordResetConfirmSerializer'
                        
                        }
REST_AUTH_REGISTER_SERIALIZERS = {
                            'REGISTER_SERIALIZER': 'authentication.api.serializer.CustomRegisterSerializer',
                        }
OLD_PASSWORD_FIELD_ENABLED = True
