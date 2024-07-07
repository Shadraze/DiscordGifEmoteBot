import os

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import FileResponse, PlainTextResponse

import base64
####

app = FastAPI()

@app.get("/gifEmote/{gif_name}")
@app.post("/gifEmote/{gif_name}")
async def supergifsOwO(gif_name: str, request : Request):
    if os.path.exists("./gifEmote/"+gif_name+".gif"):
        return FileResponse("gifEmote/"+gif_name+".gif")
        
    return await noGifEmote()   

@app.get("/gifEmote/")
@app.post("/gifEmote/")
async def noGifEmote():        
    return PlainTextResponse("Emote not found. ", 404)    


@app.post("/gifEmoteTake/")
async def gifEmoteTake(request : Request):
    requestJson = await request.json()
    filename = requestJson["filename"]
    b64data = str(requestJson["data"])

    b64data_bytes = base64.b64decode(b64data)

    with open("./gifEmote/"+filename+".gif", "+bw") as file:
        file.write(b64data_bytes)

    return PlainTextResponse("Success", 200)

