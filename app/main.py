from fastapi import FastAPI
from app.routers import plants
from app.routers import assets

# Create the FastAPI application FIRST
app = FastAPI(
    title="OT AI Platform",
    version="1.0"
)

# Register routers
app.include_router(plants.router)
app.include_router(assets.router)

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to OT AI Platform"}

# Health endpoint
@app.get("/health")
def health():
    return {"status": "Healthy"}
