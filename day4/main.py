# -*- coding: utf-8 -*-
import uvicorn
import sys
import os
import json
from application import app


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
