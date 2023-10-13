from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('myproj')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'

app.autodiscover_tasks()
