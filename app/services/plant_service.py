from app.models.plant import Plant
from app.utils.logger import logger

plants = [
    Plant(id=1, name="Panchla", location="Howrah"),
    Plant(id=2, name="Uluberia", location="Howrah")
]

def get_all_plants():
    logger.info("Fetching all plants")
    return plants

def add_plant(plant: Plant):
    logger.info(f"Adding plant: {plant.name}")

    plants.append(plant)

    return plant
