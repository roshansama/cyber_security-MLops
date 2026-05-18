from fastapi import FastAPI

from api.prediction_router import (
    router
)


app = FastAPI(

    title="Adaptive IDS API",

    version="1.0"
)


@app.get("/")

def home():

    return {

        "message":
        "Adaptive IDS API Running"
    }


@app.get("/health")

def health():

    return {

        "status":
        "healthy"
    }


app.include_router(
    router
)