"""FastAPI application for the FruitVideo AI backend."""

import logging

from fastapi import FastAPI

from app import __version__
from app.schemas import HealthResponse, ServiceResponse, VideoRequest, VideoResponse
from app.services import generate_demo_video

LOGGER = logging.getLogger(__name__)

app = FastAPI(
    title="FruitVideo AI API",
    summary="A clean API foundation for prompt-based fruit video generation.",
    description=(
        "The current version validates a text prompt and returns a demonstration "
        "video. A generative AI model can be connected through the service layer."
    ),
    version=__version__,
)


@app.get("/", response_model=ServiceResponse, tags=["Service"])
def read_root() -> ServiceResponse:
    """Return service information and the interactive documentation path."""

    return ServiceResponse(
        name="FruitVideo AI API",
        version=__version__,
        message="FruitVideo AI backend is running.",
        documentation="/docs",
    )


@app.get("/health", response_model=HealthResponse, tags=["Service"])
def health_check() -> HealthResponse:
    """Confirm that the API process is healthy."""

    return HealthResponse()


@app.post("/generate", response_model=VideoResponse, tags=["Generation"])
def generate_video(request: VideoRequest) -> VideoResponse:
    """Validate a prompt and return the current demonstration video."""

    LOGGER.info("Received a video generation request")
    video_url = generate_demo_video(request.prompt)

    return VideoResponse(
        prompt=request.prompt,
        video_url=video_url,
        message="Demo response returned; AI model integration is the next step.",
    )
