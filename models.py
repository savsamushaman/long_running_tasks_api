from pydantic import BaseModel


class Task(BaseModel):
    item_id: str
