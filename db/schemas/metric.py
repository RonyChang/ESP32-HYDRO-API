from datetime import datetime
from pydantic import BaseModel


class MetricBase(BaseModel):
    sensor_type: str
    value: float


class MetricCreate(MetricBase):
    pass

class Metric(MetricBase):
    id: int

    class Config:
        orm_mode = True
