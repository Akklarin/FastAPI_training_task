"""Dependency injection for database session in the URL Shortener project.

This module defines a dependency for obtaining an asynchronous database session.
"""

from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session

# Dependency for injecting the database session into endpoints
SessionDep = Annotated[AsyncSession, Depends(get_session)]
