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