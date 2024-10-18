from typing import Union
 
from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Guten Tag Frau Pyzh, Ich möchte dich küssen :) "}