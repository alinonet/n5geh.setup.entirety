"""
Django settings for entirety project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from typing import Optional, Dict, Any

from pydantic import (
    BaseSettings,
    PostgresDsn, validator, Field
)
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class SettingsFromEnvironment(BaseSettings):
    """Defines environment variables with their types and optional defaults"""

    # Database settings
    DATABASE_USER: str = Field(env="DATABASE_USER", default="postgres",
                         description="Postgresql connection user name")
    DATABASE_PASSWORD: str = Field(env="DATABASE_PASSWORD", default="postgres",
                             description="Postgresql connection user "
                                         "password")
    DATABASE_SERVER: str = Field(env="DATABASE_SERVER", default="localhost",
                           description="Postgresql connection server "
                                       "name")
    DATABASE_PORT: str = Field(env="DATABASE_PORT", default="5432",
                         description="Postgresql connection server port")
    DATABASE_NAME: str = Field(env="DATABASE_NAME", default="postgres",
                         description="Postgresql connection database name")
    DATABASE_URL: PostgresDsn = None

    # Debug settings
    DEBUG: bool = Field(env="DEBUG", default=False,
                        description="A boolean that turns on/off debug mode."
                                    "Don't deploy a site into production with"
                                    "DEBUG turned on")

    # Precedence of DATABASE_URL over individual settings of database.
    @validator('DATABASE_URL', pre=True)
    def create_postgres_uri(cls, v: Optional[str],
                            values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_SERVER"),
            path=f"/{values.get('DATABASE_NAME') or ''}",
            port=f"{values.get('DATABASE_PORT')}",
        )

    class Config:
        """Defines configuration for pydantic environment loading"""
        env_file = str(BASE_DIR / ".env")
        case_sensitive = True


config = SettingsFromEnvironment()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_8e5-lw61o*9ml#eds^!-wc%0g7kabh^8go)!_(7)8x13+fort"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "compressor",
    "projects.apps.ProjectsConfig",
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

ROOT_URLCONF = "entirety.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "entirety.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

os.environ["DATABASE_URL"] = config.DATABASE_URL
DATABASES = {
    'default': dj_database_url.config()
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_FINDERS = ["compressor.finders.CompressorFinder"]

COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
