from fastapi import APIRouter, HTTPException, Query
from Schemas.schemas import ProductResponse

from Services.services import (
    read_root,
    create_product_data,
)

router = APIRouter()

@router.get("/get", response_model=list[ProductResponse])
async def read_all_products():
    try:
        return read_root()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/add",response_model=ProductResponse)
async def adding_a_product(name,description,price):
    try:
        product= create_product_data(name,description,price)
        return product + HTTPException(status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))