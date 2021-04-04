from fastapi import FastAPI
from random import randint
from models import Task

app = FastAPI()
db = []


@app.get('/')
def index():
    return db


@app.post('/tasks')
def create_task(task: Task):
    """Saves the posted data in dict form to the db """
    # implement push to celery
    new_entry = task.dict()
    new_entry['task_id'] = f'task_{new_entry["item_id"][0:5]}_{randint(0, 1_000_000)}'
    db.append(new_entry)
    return db[-1]['task_id']


@app.get("/tasks/{task_id}")
def get_single_task(task_id: str):
    for task in db:
        if task['task_id'] == task_id:
            return task
    return {'Not found'}
