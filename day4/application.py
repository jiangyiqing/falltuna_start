# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.endpoint import api_router
from app.core.app_log import get_logger

app = FastAPI()
app.include_router(api_router)

#: allow cors
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
main_logger = get_logger()


@app.get('/help')
async def health_check():
    return {"message": "Hello World"}
