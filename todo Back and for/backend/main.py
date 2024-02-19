from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import database.mongo_driver as mdb
from routes import todos_api,user_api


@asynccontextmanager
async def lifespan(app: FastAPI):
    await mdb.mongodb_connect()
    yield
    # clean up resources here

app = FastAPI(
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(todos_api.router)
app.include_router(user_api.router)