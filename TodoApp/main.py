from fastapi import FastAPI, Request, status
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles 
from fastapi.responses import RedirectResponse


app = FastAPI()

Base.metadata.create_all(bind=engine)


app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static") 
# 给 /static 挂载路径起名字为 static
# 这样在 templates 中就可以用 url_for("static", path="img/xxx.png") 来引用静态文件了
# 得到的路径结果是 /static/img/xxx.png


@app.get("/")
def test(request: Request): # Jinja2Templates 需要 request 对象 作为参数 
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)