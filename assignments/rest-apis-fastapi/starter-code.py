from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# Define the Task model
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# In-memory storage for tasks
tasks_db: List[Task] = []
next_id: int = 1

# TODO: Implement GET endpoint to retrieve all tasks
# @app.get("/tasks")
# async def get_tasks():
#     pass

# TODO: Implement POST endpoint to create a new task
# @app.post("/tasks")
# async def create_task(task: Task):
#     pass

# TODO: Implement GET endpoint to retrieve a specific task by id
# @app.get("/tasks/{task_id}")
# async def get_task(task_id: int):
#     pass

# TODO: Implement PUT endpoint to update a task
# @app.put("/tasks/{task_id}")
# async def update_task(task_id: int, task: Task):
#     pass

# TODO: Implement DELETE endpoint to remove a task
# @app.delete("/tasks/{task_id}")
# async def delete_task(task_id: int):
#     pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
