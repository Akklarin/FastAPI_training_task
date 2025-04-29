from fastapi import APIRouter
from urlshort.views import urlshort_router

main_router = APIRouter()

main_router.include_router(urlshort_router)