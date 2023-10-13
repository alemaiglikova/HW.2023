from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('myproj')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'pyamqp://guest:guest@localhost//'

app.autodiscover_tasks()
