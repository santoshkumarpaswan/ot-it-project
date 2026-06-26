from fastapi import APIRouter, HTTPException
from app.models.plant import Plant
from app.services import plant_service

router = APIRouter()


# Get all plants
@router.get("/plants")
def get_plants():
    return plant_service.get_all_plants()

# Get plant by ID
@router.get("/plants/{plant_id}")
def get_plant(plant_id: int):
    for plant in plants:
        if plant.id == plant_id:
                return plant_service.get_all_plants()

    raise HTTPException(
        status_code=404,
        detail="Plant not found"
    )

# Add a new plant
@router.post("/plants")
def add_plant(plant: Plant):
    plant_service.add_plant(plant)
    return {
        "message": "Plant added successfully",
        "plant": plant
    }

# Update a plant
@router.put("/plants/{plant_id}")
def update_plant(plant_id: int, updated_plant: Plant):
    for index, plant in enumerate(plants):
        if plant.id == plant_id:
            plants[index] = updated_plant
            return {
                "message": "Plant updated successfully",
                "plant": updated_plant
            }

    raise HTTPException(
        status_code=404,
        detail="Plant not found"
    )

# Delete a plant
@router.delete("/plants/{plant_id}")
def delete_plant(plant_id: int):
    for plant in plants:
        if plant.id == plant_id:
            plants.remove(plant)
            return {"message": "Plant deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Plant not found"
    )
