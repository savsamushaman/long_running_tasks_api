from pydantic import BaseModel


# write your models here

class Task(BaseModel):
    item_id: str
