from pydantic import BaseModel 
from datetime import datetime

class Product(BaseModel):
    '''
    id, name, description, price
    '''
    created_at: datetime
    id:str
    name:str
    description:str
    price:float
    link_id:str
