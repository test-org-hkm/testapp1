from fastapi import FastAPI
import random

app = FastAPI(title="Simple FastAPI App")

@app.get("/")
def read_root():
    return {"message": "Welcome to Simple FastAPI App"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/random")
def get_random_number():
    return {"random_number": random.randint(1, 100)} 
