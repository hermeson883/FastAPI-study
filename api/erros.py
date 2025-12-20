from fastapi import FastAPI, HTTPException
from models.exceptions import UvicornException
from fastapi.requests import Request
from fastapi.responses import JSONResponse # Usado para enviar um status HTTP manualmente

app = FastAPI()

@app.exception_handler(UvicornException)
async def uvicorn_exception_handler(request: Request, exc: UvicornException):
    return JSONResponse(
        status_code=408,
        content={
            "message": f"Ops! {exc.name} did something. There goes a rainbow..."
        }
    )

@app.get("/item/{name}")
async def read_uvicorn(name: str):
    if name == "yolo":
        raise UvicornException(name=name)
    return {
        "uvicorn_name": name
    }