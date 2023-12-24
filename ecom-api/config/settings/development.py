from .base import *

DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
]
CORS_ALLOW_HEADERS = ["AUTHTOKEN", "content-type"]
