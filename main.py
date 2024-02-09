import portfolio
from fastapi import FastAPI
from portfolio.about.views import web_about

app = FastAPI()
app.include_router(web_about)

@app.get("/")
def read_root():
    return {"Hello": "World"}