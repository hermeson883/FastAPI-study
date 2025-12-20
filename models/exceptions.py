from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request

class UvicornException(Exception):
    def __init__(self, name: str):
            self.name = name