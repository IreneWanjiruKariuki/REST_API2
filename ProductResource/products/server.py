from fastapi import FastAPI
from routes import routes

products = FastAPI()

PRODUCTS_URL = "https://127.0.0.1:8000/products/"

products.include_router(routes.router)
# Entry endpoint 
@products.get("/get")
def read_root():
    return {"message": "Welcome to the REST Products API using FastAPI"}

@products.post("/add")
def create_product_data():
    return {"message": "Add new product data here"}