# -*- coding: utf-8 -*-
"""
api for xcx 
"""
from fastapi import APIRouter
from fastapi import UploadFile, File
from app.control.crud_users import *
from app.models.schema import *

router = APIRouter()


@router.get('/get-by-code')
def get_by_code(code: str):
    return {'code': code}


@router.get('/get-by-id')
def get_by_id(id):
    res = get_ftuser(id)
    print('res', res)
    return {'res': res}
