from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from internal import authentication, registration
from routers import url, contact_us, utility

models.Base.metadata.create_all(engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "URL Shortnal-Shorten your links with ease using our free URL shortener"})


@app.get("/login", response_class=HTMLResponse)
def loginUser(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request, "title": "Login"})


@app.get("/register", response_class=HTMLResponse)
def loginUser(request: Request):
    return templates.TemplateResponse("sign_up.html", {"request": request, "title": "Sign Up"})


@app.get("/dashboard.html", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "title": "Dashboard-Manage your link"})


@app.get("/contact_us", response_class=HTMLResponse)
def contactUs(request: Request):
    return templates.TemplateResponse("contact_us.html", {"request": request, "title": "Contact Us"})


app.include_router(authentication.router)
app.include_router(registration.router)
app.include_router(url.router)
app.include_router(contact_us.router)
app.include_router(utility.router)
