from fastapi import FastAPI
from src.math_ops import add, divide

app = FastAPI()

@app.get("/add")
async def add_endpoint(a: float, b: float):
    return {"result": add(a, b)}

@app.get("/divide")
async def divide_endpoint(a: float, b: float):
    return {"result": divide(a, b)}
