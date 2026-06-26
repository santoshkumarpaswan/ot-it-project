from fastapi import APIRouter

router = APIRouter()

assets = [
    {
        "id":1,
        "name":"PLC-1",
        "vendor":"Siemens"
    },
    {
        "id":2,
        "name":"Switch-1",
        "vendor":"Cisco"
    }
]

@router.get("/assets")
def get_assets():
    return assets
