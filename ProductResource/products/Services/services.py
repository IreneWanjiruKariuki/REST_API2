import requests
from Schemas.schemas import ProductResponse

PRODUCTS_URL = "http://127.0.0.1:8000/products/"

def read_root() -> list[ProductResponse]:
    response = requests.get(f"{PRODUCTS_URL}/get")
    response.raise_for_status()
    products = response.json()
    return [
        ProductResponse(
            
            name=product["name"],
            description=product.get("description","Unknown")[0],
            price=product.get("price", 0),
            
        )
        for product in products
    ]

def create_product_data(name,description,price) -> ProductResponse:
    
    product_data= {"name": name,
                   "description": description,
                   "price": price}
    response = requests.post(f"{PRODUCTS_URL}/add",json=product_data)
    response.raise_for_status()
    product = response.json()
    
    return ProductResponse(
            name=product["name"],
            description=product.get("description","Unknown"),
            price=product.get("price", 0.00),
        )
        