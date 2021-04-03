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

RADICAL_STROKE_DATA = 'kanjiRadicalStrokeData.json'
KANJI_STROKE_DATA = 'kanjiStrokeData.json'

with open(os.path.join(DATA_BASE_DIR,RADICAL_STROKE_DATA),'r') as jsonFile:
    global_radicalDict = json.load( jsonFile);
    
with open(os.path.join(DATA_BASE_DIR,KANJI_STROKE_DATA),'r') as jsonFile:
    global_kanjiDict = json.load( jsonFile);


app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello World! It works! But now, go away!"}


@app.get("/OrangeMoon/rest/getKanjiRadicals")
async def provide_kanji_radicals():
    return {'values':global_radicalDict['list'] }

@app.get("/OrangeMoon/rest/getKanjiRadicalsWithStrokes")
async def provide_kanji_radicals_with_strokes():
    return global_radicalDict

def and_set(a,b):
    return a & b

def or_set(a,b):
    return a | b

# This is quite slow, but ist just a proof of concept - the results are
# but the kanji are grouped by stroke order and as second criteria by frequency
# but the access performance can be improved 
def sort_by_globalKanji(remaining_kanji):
    global global_kanjiDict
    result = []
    for kanji in global_kanjiDict['list']:
        if kanji in remaining_kanji:
            result.append(kanji)
    return result


@app.get("/OrangeMoon/rest/getKanjiBySelectedRadicals")
async def provide_kanji_by_radical_selection(selected:str=''):
    global myJamDict
    trimmed = selected.strip()
    
    if len(trimmed)== 0:
        return {'values':[]}
    
    filtered_radicals = list(filter(lambda candidate : candidate in global_radicalDict['list'], trimmed ))
    
    if len(filtered_radicals)==0:
        return {'values':[]}
    
    radical_sets = map(lambda candidate: myJamDict.radk[candidate], filtered_radicals)
    selected_kanji = reduce ( and_set, radical_sets)
    
    sorted_selected_kanji = sort_by_globalKanji(selected_kanji)
    
    return {'values':sorted_selected_kanji }


@app.get("/OrangeMoon/rest/getKanjiBySelectedRadicals2")
async def provide_kanji_by_radical_selection_ii(selected:str=''):
    global myJamDict
    global global_radicalDict
    trimmed = selected.strip()
    
    if len(trimmed)== 0:
        return {'values':[], 'remaining_radicals':global_radicalDict['list']}
    
    filtered_radicals = list(filter(lambda candidate : candidate in global_radicalDict['list'], trimmed ))
    
    if len(filtered_radicals)==0:
        return {'values':[], 'remaining_radicals':global_radicalDict['list']}

    radical_sets = map(lambda candidate: myJamDict.radk[candidate], filtered_radicals)
    remaining_kanji = reduce ( and_set, radical_sets)
    
    sorted_remaining_kanji = sort_by_globalKanji(remaining_kanji)
    
    allRemainingRadicalSet = [set(myJamDict.krad[x]) for x in remaining_kanji]
    
    remaining_radicals = reduce(or_set, allRemainingRadicalSet)
    return {'values': sorted_remaining_kanji, 'remaining_radicals':remaining_radicals }

@app.get("/OrangeMoon/rest/strictLookupKanji")
async def lookup_kanji(selected:str=''):
    global myJamDict
    
    trimmed = selected.strip()
    
    result = myJamDict.lookup(trimmed, strict_lookup=True, lookup_ne=True)
    
    return result.to_json()

quiz_list = [
    {'name':'Grade 1', 'items':80},
    {'name':'Grade 2', 'items':160},
    {'name':'Grade 3', 'items':200},
    {'name':'Grade 4', 'items':200},
    {'name':'Grade 5', 'items':185},
    {'name':'Grade 6', 'items':181} ]

@app.get("/OrangeMoon/rest/getQuizList")
async def get_quiz_list():
    return { 'values': quiz_list}


@app.get("/OrangeMoon/rest/getQuizData")
async def get_quiz_data(quizname: str):
    for item in quiz_list:
        if item['name']==quizname:
            with open(os.path.join(DATA_BASE_DIR, 'quiz_data',item['name']+".json"), 'r') as jsonFile:
                return json.load(jsonFile) 
                # otherwise load json and return json
            pass
        
    # TODO: 404
    pass 