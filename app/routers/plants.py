from fastapi import APIRouter

router = APIRouter()

plants = [
    {"id":1,"name":"Panchla"},
    {"id":2,"name":"Uluberia"}
]

@router.get("/plants")
def get_plants():
    return plants
