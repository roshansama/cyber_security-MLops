from fastapi import FastAPI

from api.prediction_router import (
    router
)

from api.batch_router import (
    router as batch_router
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

app.include_router(
    batch_router
)



