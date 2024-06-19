from fastapi import APIRouter
from api.routes import route_metric

api_router = APIRouter()


api_router.include_router(route_metric.router, prefix="", tags=["sensors"])
