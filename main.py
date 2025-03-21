from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/{appointments}")
async def read_html(request: Request,appointments: str):
    return templates.TemplateResponse(f"{appointments}.html", {"request": request})

    