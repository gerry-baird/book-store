from fastapi import FastAPI
from routers import books

app = FastAPI()

# Include routers
app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
