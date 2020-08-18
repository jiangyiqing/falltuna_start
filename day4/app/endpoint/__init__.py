from fastapi import APIRouter
from . import xcx

api_router = APIRouter()

api_router.include_router(xcx.router, prefix="/xcx", tags=["xcx"])
