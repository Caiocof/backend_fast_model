from fastapi import FastAPI

from src.routes.example_routes import v1_example


def include_routes(app: FastAPI):
    app.include_router(v1_example)
