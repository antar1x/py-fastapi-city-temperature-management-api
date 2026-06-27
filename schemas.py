from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CityBase(BaseModel):
    name: str
    additional_info: str

class CityCreate(CityBase):
    pass

class CityRead(CityBase):
    id: int
    name: str
    additional_info: str
    model_config = ConfigDict(from_attributes=True)

class CityPartialUpdate(BaseModel):
    name: str | None = None
    additional_info: int | None = None

class TemperatureRead(BaseModel):
    id: int
    date_time: datetime
    city_id: int
    temperature: float

    model_config = ConfigDict(from_attributes=True)

