from pydantic import BaseModel

class ProductResponse(BaseModel):
    name: str
    description: str
    price: float
    
    class Config:
        from_attributes = True