"""Pydantic schemas for request and response models in the URL Shortener project."""

from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    """
    Schema for creating a short URL.

    Attributes:
        original_url (HttpUrl): The original long URL to be shortened.
    """
    original_url: HttpUrl


class URLResponse(BaseModel):
    """
    Schema for the response containing the shortened URL.

    Attributes:
        short_url (str): The generated short URL.
    """
    short_url: str
