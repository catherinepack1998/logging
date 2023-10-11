from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-7a5d%)o!ohq@r*a2+v%)4_uobxn)80@9x0w5bpr(9w@d(=pciq'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'loggerproj.urls'

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

WSGI_APPLICATION = 'loggerproj.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
        'info': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
        'warning': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
        'error_and_critical': {
            'format': ' {asctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'error_and_critical_email': {
            'format': '{levelname} {message} {pathname}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    'handlers': {
        'error_email_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ["require_debug_false"],
            'formatter': 'error_and_critical_email'
        },
        'info_file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': "logs/general.log",
            'formatter': 'info'
        },
        'error_file_errors': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': "logs/errors.log",
            'formatter': 'error_and_critical'
        },
        'info_file_security': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': "logs/security.log",
            'formatter': 'info'
        },
        'debug_console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug'
        },
        'warning_console': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning'
        },
        'error_console': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_and_critical'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['debug_console', 'warning_console', 'error_console', 'info_file_general'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['error_file_errors', 'error_email_admins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['error_file_errors', 'error_email_admins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['error_file_errors'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['error_file_errors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['info_file_security'],
            'propagate': True,
        },
    },
}