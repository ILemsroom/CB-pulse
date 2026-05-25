from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/auth/login")
def login(request: Request):
    return templates.TemplateResponse(request, "auth/login.html")


@app.get("/auth/register")
def register(request: Request):
    return templates.TemplateResponse(request, "auth/register.html")
