from datetime import datetime
from sqlalchemy import text
from sqlalchemy.orm import Session
from db.models.metric import Metric
from db.schemas.metric import MetricCreate




def get_current_time():
    return datetime.now()

def create_sensor_data(metric: MetricCreate, db: Session):
    current_time = get_current_time()
    db_sensor_data = Metric(
        record_time=current_time,
        value=metric.value,
        sensor_type=metric.sensor_type
    )
    db.add(db_sensor_data)
    db.commit()
    db.refresh(db_sensor_data)
    return db_sensor_data


def get_sensor_data(db: Session, sensor_type: str):
    return db.query(Metric).filter(Metric.sensor_type == sensor_type).first()


def get_all_sensor_data(db: Session, sensor_type: str, skip: int = 0, limit: int = 100):
    return db.query(Metric).filter(Metric.sensor_type == sensor_type).offset(skip).limit(limit).all()
    
def get_last_metric_from_sensor(db: Session, sensor_type: str):
    sensor_metrics = db.query(Metric).filter(Metric.sensor_type == sensor_type).all()
    last_metric = sensor_metrics[-1]
    return last_metric

def get_all_sensor_data_all(db: Session):
    return db.query(Metric).all()

def delete_all_sensor_data(db: Session, sensor_type: str):
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

def delete_all_sensor_data_all(db: Session):
    db.query(Metric).delete()
    db.commit()