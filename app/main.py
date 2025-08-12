from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(todo_router)
register_tortoise(
    app=app,
    db_url = "sqlite://todo.db",
    add_exception_handlers=True,
    generate_schemas = True,
    modules ={"models":["api.models.todo"]}
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica dominios exactos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return{"status": "is running"}