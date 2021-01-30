from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from data.links import data as links


app = FastAPI()


@app.get("/twitch")
async def twitch():
    return RedirectResponse(links["twitch"])


@app.get("/twitter")
async def twitter():
    return RedirectResponse(links["twitter"])


@app.get("/telegram")
async def telegram():
    return RedirectResponse(links["telegram"])


@app.get("/github")
async def github():
    return RedirectResponse(links["github"])
