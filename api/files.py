from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()

@app.post("/files/")
async def create_file(files: Annotated[list[bytes], File(description="Multiple read a Bytes")]):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfile/")
async def create_upload(files: Annotated[list[UploadFile], File(description="Multiple files as UploadFile")]):
    return {"filenames": [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
        <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)