from fastapi import FastAPI

from .routers import forecasts

app = FastAPI()


app.include_router(forecasts.router)
