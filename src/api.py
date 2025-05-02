"""Main API router setup for the FastAPI URL Shortener project.

This module creates the root API router and includes all sub-routers.
"""

from fastapi import APIRouter
from src.urlshort.views import urlshort_router

main_router = APIRouter()

main_router.include_router(urlshort_router)
