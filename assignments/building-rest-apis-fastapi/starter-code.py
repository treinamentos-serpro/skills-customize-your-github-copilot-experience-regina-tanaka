from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="Task API")


class Task(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    description: str | None = None
    completed: bool | None = None


tasks: dict[int, Task] = {
    1: Task(title="Explorar a documentação", description="Visitar /docs"),
}


@app.get("/")
def read_root():
    return {"message": "Task API is running"}


@app.get("/tasks")
def list_tasks():
    return [{"id": task_id, **task.model_dump()} for task_id, task in tasks.items()]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": task_id, **task.model_dump()}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    new_id = max(tasks, default=0) + 1
    task = Task(**task_data.model_dump())
    tasks[new_id] = task
    return {"id": new_id, **task.model_dump()}


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_data = task.model_dump()
    updated_data.update(task_data.model_dump(exclude_unset=True))
    updated_task = Task(**updated_data)
    tasks[task_id] = updated_task
    return {"id": task_id, **updated_task.model_dump()}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if tasks.pop(task_id, None) is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}