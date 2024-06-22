from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
from db.session import get_db
from db.schemas.metric import Metric, MetricCreate
from db.repository.metric import create_sensor_data, get_sensor_data, get_all_sensor_data, get_all_sensor_data_all, get_last_metric_from_sensor, delete_all_sensor_data, delete_all_sensor_data_all

#PH, TDS, TAGUA, HAMB, TAMB, TAGUA,INTENSIDAD LUMINICA(LUM)

router = APIRouter()


@router.post("/metric/create-metric/", response_model=Metric)
def create_sensor_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    return create_sensor_data(db=db, metric=metric)


@router.get("/metrics/get-last-metric-from-sensor/{sensor_type}", response_model=Metric)
def read_metric_from_sensor(sensor_type: str, db: Session = Depends(get_db)):
    db_sensor_data = get_last_metric_from_sensor(db=db, sensor_type=sensor_type)
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="Temp_Amb not found")
    return db_sensor_data

@router.get("/metrics/get-metrics-from-sensor/{sensor_type}", response_model=list[Metric])
def read_all_metrics_from_sensor(sensor_type: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_all_sensor_data(db, sensor_type=sensor_type, skip=skip, limit=limit)
    return metrics
    
# Endpoint para obtener los últimos datos de todos los sensores
@router.get("/sensors/last", response_model=list[Metric])
def read_last_sensors_data(db: Session = Depends(get_db)):
    last_sensors_data = get_last_metric_from_all_sensors(db=db)
    if not last_sensors_data:
        raise HTTPException(status_code=404, detail="No sensor data found")
    return last_sensors_data

# Endpoint para obtener todos los datos de todos los sensores
@router.get("/sensors/all", response_model=list[Metric])
def read_all_sensors(db: Session = Depends(get_db)):
    sensors_data = get_all_sensor_data_all(db=db)
    if not sensors_data:
        raise HTTPException(status_code=404, detail="No sensor data found")
    return sensors_data

@router.delete("/metrics/delete-metrics-from-sensor/{sensor_type}")
def delete_all_metrics_from_sensor(sensor_type: str, db: Session = Depends(get_db)):
    return delete_all_sensor_data(db=db, sensor_type=sensor_type)

# Endpoint para borrar todos los datos de todos los sensores
@router.delete("/delete-sensors/all")
def delete_all_sensors(db: Session = Depends(get_db)):
    delete_all_sensor_data_all(db=db)
    return {"message": "All sensor data deleted successfully"}


"""
# Sensor Temperatura ambiente
@router.post("/temp_amb/create", response_model=Metric)
def create_temp_amb(sensor_data: MetricCreate, db: Session = Depends(get_db)):
    return create_sensor_data(db=db, sensor_type="temp_amb", sensor_data=sensor_data)

@router.get("/temp_amb/{sensor_data_id}", response_model=Metric)
def read_metric(sensor_data_id: int, db: Session = Depends(get_db)):
    db_sensor_data = get_sensor_data(db=db, sensor_type="temp_amb", sensor_data_id=sensor_data_id)
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="Temp_Amb not found")
    return db_sensor_data

@router.get("/temp_amb", response_model=list[Metric])
def read_temp_amb(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_all_sensor_data(db, sensor_type="temp_amb", skip=skip, limit=limit)
    return metrics

@router.delete("/temp_amb")
def delete_temp_amb(db: Session = Depends(get_db)):
    return delete_all_sensor_data(db=db, sensor_type="temp_amb")

# Sensor Humedad ambiente

@router.post("/hum_amb/create", response_model=Metric)
def create_hum_amb(sensor_data: MetricCreate, db: Session = Depends(get_db)):
    return create_sensor_data(db=db, sensor_type="hum_amb", sensor_data=sensor_data)

@router.get("/hum_amb/{sensor_data_id}", response_model=Metric)
def read_metric(sensor_data_id: int, db: Session = Depends(get_db)):
    db_sensor_data = get_sensor_data(db=db, sensor_type="hum_amb", sensor_data_id=sensor_data_id)
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="hum_Amb not found")
    return db_sensor_data

@router.get("/hum_amb", response_model=list[Metric])
def read_hum_amb(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_all_sensor_data(db, sensor_type="hum_amb", skip=skip, limit=limit)
    return metrics

@router.delete("/hum_amb")
def delete_hum_amb(db: Session = Depends(get_db)):
    return delete_all_sensor_data(db=db, sensor_type="hum_amb")

# Sensor Temperatura agua

@router.post("/temp_agua/create", response_model=Metric)
def create_temp_agua(sensor_data: MetricCreate, db: Session = Depends(get_db)):
    return create_sensor_data(db=db, sensor_type="temp_agua", sensor_data=sensor_data)

@router.get("/temp_agua/{sensor_data_id}", response_model=Metric)
def read_metric(sensor_data_id: int, db: Session = Depends(get_db)):
    db_sensor_data = get_sensor_data(db=db, sensor_type="temp_agua", sensor_data_id=sensor_data_id)
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="Temp_agua not found")
    return db_sensor_data

@router.get("/temp_agua", response_model=list[Metric])
def read_temp_agua(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_all_sensor_data(db, sensor_type="temp_agua", skip=skip, limit=limit)
    return metrics

@router.delete("/temp_agua")
def delete_temp_agua(db: Session = Depends(get_db)):
    return delete_all_sensor_data(db=db, sensor_type="temp_agua")

# Sensor PH

@router.post("/ph/create", response_model=Metric)
def create_ph(sensor_data: MetricCreate, db: Session = Depends(get_db)):
    return create_sensor_data(db=db, sensor_type="ph", sensor_data=sensor_data)

@router.get("/ph/{sensor_data_id}", response_model=Metric)
def read_metric(sensor_data_id: int, db: Session = Depends(get_db)):
    db_sensor_data = get_sensor_data(db=db, sensor_type="ph", sensor_data_id=sensor_data_id)
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="PH not found")
    return db_sensor_data

@router.get("/ph", response_model=list[Metric])
def read_ph(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_all_sensor_data(db, sensor_type="ph", skip=skip, limit=limit)
    return metrics

@router.delete("/ph")
def delete_ph(db: Session = Depends(get_db)):
    return delete_all_sensor_data(db=db, sensor_type="ph")

# Sensor TDS

@router.post("/tds/create", response_model=Metric)
def create_tds(sensor_data: MetricCreate, db: Session = Depends(get_db)):
    return create_sensor_data(db=db, sensor_type="tds", sensor_data=sensor_data)

@router.get("/tds/{sensor_data_id}", response_model=Metric)
def read_metric(sensor_data_id: int, db: Session = Depends(get_db)):
    db_sensor_data = get_sensor_data(db=db, sensor_type="tds", sensor_data_id=sensor_data_id)
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="TDS not found")
    return db_sensor_data

@router.get("/tds", response_model=list[Metric])
def read_tds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_all_sensor_data(db, sensor_type="tds", skip=skip, limit=limit)
    return metrics

@router.delete("/tds")
def delete_tds(db: Session = Depends(get_db)):
    return delete_all_sensor_data(db=db, sensor_type="tds")

# Sensor Intensidad Lumínica

@router.post("/lum/create", response_model=Metric)
def create_lum(sensor_data: MetricCreate, db: Session = Depends(get_db)):
    return create_sensor_data(db=db, sensor_type="lum", sensor_data=sensor_data)

@router.get("/lum/{sensor_data_id}", response_model=Metric)
def read_metric(sensor_data_id: int, db: Session = Depends(get_db)):
    db_sensor_data = get_sensor_data(db=db, sensor_type="lum", sensor_data_id=sensor_data_id)
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="Lum not found")
    return db_sensor_data

@router.get("/lum", response_model=list[Metric])
def read_lum(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_all_sensor_data(db, sensor_type="lum", skip=skip, limit=limit)
    return metrics

@router.delete("/lum")
def delete_lum(db: Session = Depends(get_db)):
    return delete_all_sensor_data(db=db, sensor_type="lum")

"""
