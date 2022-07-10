from fastapi import FastAPI
from src.routes.routes import include_routes

app = FastAPI()

include_routes(app=app)


@app.get("/")
async def root():
    return {"message": "Hello World"}
