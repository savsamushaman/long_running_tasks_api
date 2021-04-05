from random import randint
from time import sleep

from celery import Celery

# write additional tasks here

app = Celery('tasks', backend='redis://redis:6379/0', broker='redis://redis:6379/0')


@app.task()
def execute_task(item_id, tasks_id):
    print(f'>>> Long Running Task of Item: {item_id} with Tasks_id : {tasks_id} started..')
    duration = randint(10, 20)
    sleep(duration)
    return duration
