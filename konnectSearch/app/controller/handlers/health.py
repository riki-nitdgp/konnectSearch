from fastapi import APIRouter

from app.utils.config import Config
from app.utils.response_utils import ResponseUtils

router = APIRouter()


@router.get("/health")
async def health_check():
    data = {"message": "{service_name} is Up Now !!".format(service_name=Config.get_config("SERVICE_NAME"))}
    return ResponseUtils.build_success_response(data)
