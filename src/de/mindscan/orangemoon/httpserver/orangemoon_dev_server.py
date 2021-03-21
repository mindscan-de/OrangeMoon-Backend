'''
Created on 21.03.2021

@author: JohnDoe
'''

SRC_BASE_DIR  = '../../../../../src'
DATA_BASE_DIR = '../../../../../data'

import sys
sys.path.insert(0,SRC_BASE_DIR)

import os
import json
import uuid as uid

from jamdict import Jamdict

from fastapi import FastAPI, Form, HTTPException
# from starlette.responses import FileResponse


app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello World! It works! But now, go away!"}

