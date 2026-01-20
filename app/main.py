from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import authors, categories, books
app = FastAPI(
    title="Book Management API",
    description="Simple Api to manage books, authors, categories and covers",
    version="1.0.0"
)
#Include Routers
app.include_router(authors.router, prefix="/authors", tags=["Authors"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(books.router, prefix="/books", tags=["Books"])

#Static files for covers images

@app.get("/")#127.0.0.1:8000
def read_root():
    return {"message": "Book Management API is running"}