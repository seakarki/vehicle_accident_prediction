from pydantic import BaseModel
class vehicleAccident(BaseModel):
    driver_age: float
    is_driver_alcholic: float
    driver_license_age: float
    vehicle_age: float
    vehicle_mileage: float