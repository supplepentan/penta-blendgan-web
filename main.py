# 必要なモジュールを読み込む
from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
import tempfile
from PIL import Image
import subprocess
import os
import zipfile
import shutil
from fastapi.params import File

import uvicorn
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import FileResponse
from io import BytesIO

from starlette.middleware.cors import CORSMiddleware


app = FastAPI(
    title='ARマーカー作成',
    description='ARマーカーを作成できるよ',
    version='1.0')

#: Configure CORS
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="./front/dist/static"), name="static")
templates = Jinja2Templates(directory="./front/dist/")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})

@app.post("/upload")
async def index(file: UploadFile = File(...)):
    contents = await file.read()
    #im = Image.open(BytesIO(contents))
    image = Image.open(BytesIO(contents)).convert('RGB')
    # アプロードされたファイルをいったんテンポラリーフォルダに保存し、app.jsを実行
    with tempfile.TemporaryDirectory(dir=".") as dname:
        filepath = dname+"/maker.jpg"
        print(filepath)
        image.save(filepath)
        # OSコマンドを実行
        subprocess.run(['node', 'app.js', '-i', filepath])
    # "output"フォルダに作成された3つのファイルをzip圧縮
    with zipfile.ZipFile(os.path.join(".", "output", "marker.zip"), 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        new_zip.write(os.path.join(".", "output", "maker.fset"), arcname="maker.fset")
        new_zip.write(os.path.join(".", "output", "maker.fset"), arcname="maker.fset3")
        new_zip.write(os.path.join(".", "output", "maker.fset"), arcname="maker.iset")
    return {"msg":"Finished"}
@app.get("/download")
async def index():
    if os.path.exists("output/marker.zip"):
        return FileResponse(path="output/marker.zip")
    else:
        return
if __name__ == "__main__":
    uvicorn.main(app=app)
