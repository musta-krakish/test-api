from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import File, UploadFile, Request
from typing import List
from utils.idf import *

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.post("/")
async def upload_file(request: Request, file: UploadFile = File(...)):
    word_count = process_file(file.file)
    documents = [word_count]
    idf_values = {word: idf(word, documents) for word in word_count}
    sorted_idf = sorted(idf_values.items(), key=lambda x: x[1], reverse=True)[:50]
    return templates.TemplateResponse("result-form.html", {"request": request, "sorted_idf": sorted_idf})

@router.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload-form.html", {"request": request})