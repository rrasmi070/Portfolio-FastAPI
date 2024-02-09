from fastapi import APIRouter
web_about = APIRouter(
    prefix="/web_about",
    tags=["about"],
    responses={404: {"description": "Not found"}},
)


@web_about.post("/add-about")
def read_root():
    return {"message": "Hello, World"}


@web_about.get("/get-about")
async def index():
    return {"message": "Hello World"}