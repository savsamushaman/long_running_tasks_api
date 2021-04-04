from random import randint
from time import sleep

from celery import Celery

# write additional tasks here

cel_app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')


@cel_app.task
def execute_task(item_id, task_id):
    print('>>> Long Running Task starting')
    duration = randint(15, 25)
    sleep(duration)
    return duration