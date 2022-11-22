from .base import *

DEBUG = False
ALLOWED_HOSTS += ["http://127.0.0.1"]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
