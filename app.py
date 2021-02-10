import logging

from fastapi import FastAPI, Request

from starlette.responses import HTMLResponse

logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/favicon.ico")
async def favicon(request: Request):
    logger.error("request %s", request.client.host)
    logger.error("favicon")


@app.get("/")
async def index():
    logger.error("in app index")
    with open("./static/index.html") as f:
        return HTMLResponse(f.read())