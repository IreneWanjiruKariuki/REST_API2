from pydantic import BaseModel

class ProductResponse(BaseModel):
    name: str
    description: str
    price: float
    
    class Config:
        orm_model = True