from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from app.web.thread_controller import router as thread_rooter
from app.web.comment_controller import router as comment_rooter

config = dotenv_values(".env")

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGO_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(thread_rooter, tags=["threads"], prefix="/threads")
app.include_router(comment_rooter, tags=["comments"], prefix="/comments")
