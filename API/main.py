"""Introduction of my code"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="titre")

class MyClass(BaseModel):
    """Data theme for example"""
    text: str

@app.get("/")
async def root():
    """Main API Route"""
    return {"message": "Hello World"}