from fastapi import FastAPI
from logger import logger
import asyncio
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
logger.info('Starting API.....')



@app.get("/")
async def index() -> dict:
    # logger.info('Request to the index page')
    return {"message": "Hello Boss"}

@app.get("/upload-videos")
async def upload_videos() -> dict:
    await asyncio.sleep(1.5)
    # logger.info('Request to the video-upload page')
    return {"message": "Video Uploaded"}

