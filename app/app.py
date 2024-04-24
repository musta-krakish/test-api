from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import file_router

app = FastAPI()

app.include_router(file_router.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
