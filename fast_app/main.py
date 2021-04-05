from celery import Celery
from celery.result import AsyncResult
from fastapi import FastAPI

from models import Task
from worker.tasks import execute_task


class TaskDataBase:
    """Burner database, DO NOT, UNDER ANY CASE USE IN PROD."""

    def __init__(self):
        self.data = []

    def add_task(self, task_dict):
        task_id = execute_task.delay(task_dict['item_id']).task_id
        task_dict['task_id'] = task_id
        self.data.append(task_dict)
        print(">>> Task successfully added to DB")

        return task_id

    def fetch(self, task_id):
        for task in self.data:
            if task['task_id'] == task_id:
                return task
        return None


app = FastAPI()
db = TaskDataBase()
cel_app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')


@app.get('/')
def index():
    return db.data


@app.post('/tasks')
def create_task(task: Task):
    """Saves the posted data in dict form to the db and returns the task_id"""
    return {'task_id': db.add_task(task.dict()),
            'hint': 'GET http://127.0.0.1:8000/tasks/{task_id} to keep track of the task'}


@app.get("/tasks/{task_id}")
def get_single_task(task_id: str):
    task = db.fetch(task_id)
    if not task:
        return {'response': 'task not found'}

    result = AsyncResult(task['task_id'], app=cel_app)

    response = {'task_id': task['task_id'], 'item_id': task['item_id'], 'status': result.status,
                'result': result.result}

    return response
