from .base import *

DEBUG = False


ALLOWED_HOSTS = ["server.glowbeyond.shop", "www.server.glowbeyond.shop"]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
]
CORS_ALLOW_HEADERS = ["AUTHTOKEN", "content-type"]
CORS_ALLOW_CREDENTIALS = True
