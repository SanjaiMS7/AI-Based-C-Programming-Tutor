from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from debugger.c_logic import process_query

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask(request: Request, query: str = Form(...)):
    result = process_query(query)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result, "query": query}
    )