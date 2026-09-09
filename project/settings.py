"""
Minimal Django settings for the DevOps practice target.

Config is read from environment variables (12-factor) where it matters
for deployment: SECRET_KEY, DEBUG, and ALLOWED_HOSTS.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- 12-factor config: read from the environment -------------------------

# A dev-friendly default so the app runs out of the box. NEVER use this
# default in production; set SECRET_KEY in the environment instead.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "dev-insecure-change-me-in-production-0123456789",
)

# DEBUG is off unless DEBUG=true/1/yes is set in the environment.
DEBUG = os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes")

# ALLOWED_HOSTS is a comma-separated list; defaults to "*" for easy dev/deploy.
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# -------------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    },
]

WSGI_APPLICATION = "project.wsgi.application"

# Default SQLite database — simple, file-based, zero config.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
