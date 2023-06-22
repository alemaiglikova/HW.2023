from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Task


app = FastAPI()

templates = Jinja2Templates(directory="templates")
@app.get("/")
def index(request: Request):
   
    db = SessionLocal()
    tasks = db.query(Task).order_by(Task.id).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/add")
def add_task(request: Request, title: str = Form(...), description: str = Form(...)):
  
    db = SessionLocal()
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return templates.TemplateResponse("redirect.html", {"request": request, "message": "Задача успешно добавлена.", "url": "/"})

@app.get("/delete/{task_id}")
def delete_task(request: Request, task_id: int):

    db = SessionLocal()
    task = db.query(Task).get(task_id)
    if task:
        db.delete(task)
        db.commit()
        db.close()
        return templates.TemplateResponse("redirect.html", {"request": request, "message": "Задача успешно удалена.", "url": "/"})
    db.close()
    return templates.TemplateResponse("redirect.html", {"request": request, "message": "Задача не найдена.", "url": "/"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

