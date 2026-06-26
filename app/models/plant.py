from pydantic import BaseModel

class Plant(BaseModel):
    id: int
    name: str
    location: str
