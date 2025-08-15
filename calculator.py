from fastapi import FastAPI, HTTPException
from typing import Union

app=FastAPI(title="Calculator API", version="1.0.0")

@app.get("/")
def root():
    return {"calculator API- use /docs for documentation"}

@app.get("/add")
def add_numbers(a:float, b:float):
    return {"result": a + b, "operation": f"{a}+{b}"}

@app.get("/subtract")
def subtract_numbers(a:float,b:float):
    return {"result": a-b, "operation": f"{a}-{b}"}

@app.post("/multiply")
def multiply_numbers(a:float,b:float):
    return{"results": a * b, "operation": f"{a}*{b}"}

@app.post("/divide")
def divide_numbers(a:float, b:float):
    if b==0:
        raise HTTPException(status_code=400, detail='Division by zero is not allowed')
    return{"result": a / b, "operation": f"{a}/{b}"}