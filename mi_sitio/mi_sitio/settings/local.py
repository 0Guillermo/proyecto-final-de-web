from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'final',
        'USER':'root',
        'PASSWORD':'guille',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
