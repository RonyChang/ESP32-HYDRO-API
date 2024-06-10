from datetime import datetime
from pydantic import BaseModel


class MetricBase(BaseModel):
    sensor_type: str
    value: float


class MetricCreate(MetricBase):
    record_time: datetime
    pass

class Metric(MetricBase):
    id: int

    class Config:
        orm_mode = True
