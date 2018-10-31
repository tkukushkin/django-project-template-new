from pathlib import Path


def path(*args: str) -> str:
    return str(Path(__file__).parent.parent.joinpath(*args))


SECRET_KEY = 'g!c=%mu!+@@8c(3f*!!#84^-%yqv)ate4p0@^owut95cg-)m@g'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',

    '{{ cookiecutter.package_name }}',
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

ROOT_URLCONF = '{{ cookiecutter.package_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': (
            path('templates'),
        ),
        'APP_DIRS': False,
        'OPTIONS': {
            'environment': '{{ cookiecutter.package_name }}.jinja2.environment'
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
            'loaders': (
                ('django.template.loaders.cached.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                )),
            ),
        }
    },
]

WSGI_APPLICATION = '{{ cookiecutter.package_name }}.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ cookiecutter.package_name }}',
    },
}

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = [path('static')]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
