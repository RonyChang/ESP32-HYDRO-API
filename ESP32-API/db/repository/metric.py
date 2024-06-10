from sqlalchemy import text
from sqlalchemy.orm import Session
from db.models.metric import Metric
from db.schemas.metric import MetricCreate


def get_sensor_data(db: Session, sensor_type: str, sensor_data_id: int):
    return db.query(Metric).filter(Metric.sensor_type == sensor_type, Metric.id == sensor_data_id).first()

def create_sensor_data(db: Session, sensor_type: str, sensor_data: MetricCreate):
    db_sensor_data = Metric(sensor_type=sensor_type, value=sensor_data.value)
    db.add(db_sensor_data)
    db.commit()
    db.refresh(db_sensor_data)
    return db_sensor_data


def get_all_sensor_data(db: Session, sensor_type: str, skip: int = 0, limit: int = 100):
    return db.query(Metric).filter(Metric.sensor_type == sensor_type).offset(skip).limit(limit).all()


def delete_all_metrics(db: Session, sensor_type: str):
    try:
        db.query(Metric).filter(Metric.sensor_type == sensor_type).delete()
        db.execute(text("DELETE FROM ESP32Metrics;"))
        db.commit()
        return {"message": "All rows deleted successfully"}
    except Exception as e:
        db.rollback()
        return {"message": f"An error occurred: {str(e)}"}
    finally:
        db.close()
