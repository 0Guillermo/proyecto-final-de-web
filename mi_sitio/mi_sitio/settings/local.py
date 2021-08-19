from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jugadores',
        'USER':'root',
        'PASSWORD':'guille',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
