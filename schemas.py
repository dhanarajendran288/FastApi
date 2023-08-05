from pydantic import BaseModel
from datetime import date



class PostUserDetails(BaseModel):
    DealDate:date
    SecurityCode:int
    SecurityName:str
    ClientName:str
    DealType :str
    Quantity:int
    Price:float

class PutUserDetails(BaseModel):
    DealDate:date
    SecurityCode:int
    SecurityName:str
    ClientName:str
    DealType :str
    Quantity:int
    Price:float
    UniqueId:int
