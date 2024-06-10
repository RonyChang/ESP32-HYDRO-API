from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
from db.session import get_db
from db.schemas.metric import Metric, MetricCreate
from db.repository.metric import create_sensor_data, get_sensor_data, get_all_sensor_data, delete_all_sensor_data

#PH, TDS, TAGUA, HAMB, TAMB, TAGUA,INTENSIDAD LUMINICA(LUM)

router = APIRouter()

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