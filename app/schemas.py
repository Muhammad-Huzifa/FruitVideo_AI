"""Request and response models for the API."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class VideoRequest(BaseModel):
    """A validated text prompt submitted for video generation."""

    model_config = ConfigDict(str_strip_whitespace=True)

    prompt: str = Field(
        ...,
        min_length=3,
        max_length=500,
        examples=["A ripe mango rotating slowly on a wooden table"],
    )


class VideoResponse(BaseModel):
    """Response returned by the current demonstration generator."""

    status: Literal["success"] = "success"
    prompt: str
    video_url: str
    demo: bool = True
    message: str


class HealthResponse(BaseModel):
    """Service health response."""

    status: Literal["healthy"] = "healthy"


class ServiceResponse(BaseModel):
    """Basic information about the running service."""

    name: str
    version: str
    message: str
    documentation: str
