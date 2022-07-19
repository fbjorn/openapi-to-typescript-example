from datetime import datetime
from typing import List, Optional
from uuid import uuid4


import pendulum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Simple Task Tracker")
db = {}


class TaskIn(BaseModel):
    title: str
    dueDate: Optional[datetime]


class Task(TaskIn):
    id: str


class Tasks(BaseModel):
    tasks: List[Task]
    count: int


@app.post("/tasks", response_model=Task, operation_id="create_task")
def create_task(data: TaskIn):
    task = Task(
        id=str(uuid4()),
        title=data.title,
        dueDate=data.dueDate or pendulum.tomorrow(),
    )
    db[task.id] = task
    return task


@app.get("/tasks", response_model=Tasks, operation_id="list_tasks")
def list_tasks():
    return Tasks(tasks=list(db.values()), count=len(db))


@app.get("/tasks/{task_id}", response_model=Task, operation_id="get_task")
def get_task(task_id: str):
    try:
        return db[task_id]
    except KeyError:
        raise HTTPException(404)
