"""Base settings settings."""
from os.path import dirname
from os.path import abspath

BASE_DIR = dirname(dirname(abspath(__file__)))

DEBUG = True

APPEND_SLASH = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'kileed.oi.lan']

ROOT_URLCONF = 'urls'

LOGIN_URL = '/api-auth/login'

SECRET_KEY = '5cc74*&^b^huo+^q-ft)+t!_(9t04$wk2r&gz*qd%r&i4gm7&d'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'webpack_loader',
    'kileed'
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

STATIC_URL = '/static/'
