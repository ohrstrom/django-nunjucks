import django
from django.conf import settings
from django.db.models import get_model, get_app

DEBUG = getattr(settings, 'NUNJUCKS_DEBUG', False)

def get_channel():
    return '%s' % SETTINGS.get('CHANNEL_PREFIX', 'nunjucks_')

