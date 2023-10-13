

from celery import shared_task
import time

@shared_task
def long_running_task(duration):
    time.sleep(duration)
    return f'Long running task finished after {duration} seconds.'
