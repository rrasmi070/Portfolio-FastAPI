import portfolio
import db
from fastapi import FastAPI
from portfolio.about.views import web_about
from dotenv import load_dotenv
load_dotenv()
import os




app = FastAPI()
app.include_router(web_about)

@app.get("/")
def read_root():
    return {"Hello": "World"}