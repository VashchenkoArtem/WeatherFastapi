from fastapi import FastAPI
from weather.routers import router

app = FastAPI()


app.include_router(router)
