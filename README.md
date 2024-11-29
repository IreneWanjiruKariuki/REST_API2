# REST_API2

A simple REST API in Python that manages a Product resource and handles JSON requests and responses.

## Prerequisites
Ensure you have the following installed in your system:
 - Python(3.12.6)
 - pip

## Setting up the environment
Follow the following steps to create and run the project:

### 1. Create a github repository
 - Go to [GitHub](https://github.com/) and create a new repository
 - Copy the repository URL

### 2. Clone the repository
 ```bash
 git clone https://github.com/IreneWanjiruKariuki/REST_API.git
 ```

 ### 3. Create and activate a virtual environment
 Create a virtual environment to isolate project dependencies:

 ```bash
 py -m venv venv
 ```

 Avtivate the virtual environment:


 ```bash
 .\venv\Scripts\Activate.ps1
 ```

 ### 4. Install requirements

 ```bash
 pip install requests fastapi uvicorn
 ```

 ### 5. Install django

 ```bash
 py -m pip install Django
 ```

 ### 6. Create a project

 ```bash
 django-admin startproject ProductResourse
 ```

 ### 7. Create app

 ```bash
 django-admin startapp products
 ```

 ### 8. Start the development server

 ```bash
 python manage.py runserver
 ```

 ## Create a model
 Create a model named Products in the app as follows:
 ```bash
 class Product(models.Model):
  name = models.CharField(max_length=100)#The name of the product
  description = models.CharField(max_length=100)#The product description
  price = models.DecimalField(max_digits=10, decimal_places=2)#The price of the product
```

## Create main.py

The code sends an HTTP GET request to a local server at http://127.0.0.1:8000/products/ using the requests library. It retrieves the response from the server and stores the raw response text in the products variable.

## Create server.py
This is where the GET and POST endpoints are created.

## Create schemas.py

This file is created inside the app folder which in thes case is the projects folder. This is where the schema of the model created is created.

```bash
from pydantic import BaseModel

class ProductsResponse(BaseModel):
    name: str
    description: str
    price: float
    
    class Config:
        orm_mode = True
```

## Create services.py
This file is created inside the app folder which in thes case is the projects folder. This is where the python scripts are written.

```bash
import requests
from Schemas.schemas import ProductResponse

PRODUCTS_URL = "http://127.0.0.1:8000/products/"

def get_all_products() -> list[ProductResponse]:
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

def add_product(name,description,price) -> ProductResponse:
    
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
```

## Create routes.py
This file is created inside the app folder which in thes case is the projects folder.

```bash
from fastapi import APIRouter, HTTPException, Query
from Schemas.schemas import ProductResponse

from Services.services import (
    get_all_products,
    add_product,
)

router = APIRouter()

@router.get("/get", response_model=list[ProductResponse])
async def read_all_products():
    try:
        return get_all_products()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/add",response_model=ProductResponse)
async def adding_a_product(name,description,price):
    try:
        product= add_product(name,description,price)
        return product + HTTPException(status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
## Testing manually
Using the browser open the link:
```bash
http://127.0.0.1:8000/docs
```

## Testing with python scripts
Run the routes.py file that contains the execution of the python scripts.