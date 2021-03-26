'''
Created on 21.03.2021

MIT License

Copyright (c) 2021 Maxim Gansert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

@autor: Maxim Gansert
'''
SRC_BASE_DIR  = '../../../../../src'
DATA_BASE_DIR = '../../../../../data'

import sys
sys.path.insert(0,SRC_BASE_DIR)

import os
import json
import uuid as uid
from functools import reduce

from jamdict import Jamdict

from fastapi import FastAPI, Form, HTTPException
# from starlette.responses import FileResponse

myJamDict = Jamdict()

global_radicalKeys=[x for x in myJamDict.radk.keys()]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello World! It works! But now, go away!"}


@app.get("/OrangeMoon/rest/getKanjiRadicals")
async def provide_kanji_radicals():
    global global_radicalKeys
    return {'values':global_radicalKeys }

def and_set(a,b):
    return a & b

def or_set(a,b):
    return a | b


@app.get("/OrangeMoon/rest/getKanjiBySelectedRadicals2")
async def provide_kanji_by_radical_selection_ii(selected:str=''):
    global myJamDict
    global global_radicalKeys
    trimmed = selected.strip()
    
    if len(trimmed)== 0:
        return {'values':[], 'remaining_radicals':global_radicalKeys}
    
    filtered_radicals = list(filter(lambda candidate : candidate in myJamDict.radk, trimmed ))
    
    if len(filtered_radicals)==0:
        return {'values':[], 'remaining_radicals':global_radicalKeys}

    radical_sets = map(lambda candidate: myJamDict.radk[candidate], filtered_radicals)
    remaining_kanji = reduce ( and_set, radical_sets)
    
    allRemainingRadicalSet = [set(myJamDict.krad[x]) for x in remaining_kanji]
    
    remaining_radicals = reduce(or_set, allRemainingRadicalSet)
    return {'values': remaining_kanji, 'remaining_radicals':remaining_radicals }
    


@app.get("/OrangeMoon/rest/getKanjiBySelectedRadicals")
async def provide_kanji_by_radical_selection(selected:str=''):
    global myJamDict
    trimmed = selected.strip()
    
    if len(trimmed)== 0:
        return {'values':[]}
    
    filtered_radicals = list(filter(lambda candidate : candidate in myJamDict.radk, trimmed ))
    
    if len(filtered_radicals)==0:
        return {'values':[]}
    
    radical_sets = map(lambda candidate: myJamDict.radk[candidate], filtered_radicals)
    selected_kanji = reduce ( and_set, radical_sets)
    
    return {'values':selected_kanji }

@app.get("/OrangeMoon/rest/getRemainingRadicalsBySelectedRadicals")
async def provide_remaining_radicals_by_radical_selection(selected:str=''):
    global myJamDict
    trimmed = selected.strip()
    
    if len(trimmed)== 0:
        return {'values':[]}
    
    filtered_radicals = list(filter(lambda candidate : candidate in myJamDict.radk, trimmed ))
    
    if len(filtered_radicals)==0:
        return {'values':[]}
    
    radical_sets = map(lambda candidate: myJamDict.radk[candidate], filtered_radicals)
    remaining_kanji = reduce ( and_set, radical_sets)
    
    allRemainingRadicalSet = [set(myJamDict.krad[x]) for x in remaining_kanji]
    
    remaining_radicals = reduce(or_set, allRemainingRadicalSet)
    return {'values':remaining_radicals }