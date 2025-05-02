"""Main application entry point for the FastAPI URL Shortener project.

This module initializes the FastAPI app with configuration settings,
includes the API router, and starts the Uvicorn server if run as the main program.
"""

from fastapi import FastAPI
from src.api import main_router
from src.urlshort.config import settings
import uvicorn

app = FastAPI(
    title=settings.PROJECT_TITLE,
    description=settings.PROJECT_DESCRIPTION,
    docs_url=settings.PROJECT_DOCS_URL
    )

app.include_router(main_router)


if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host=settings.PROJECT_HOST,
        port=settings.PROJECT_PORT,
    )
