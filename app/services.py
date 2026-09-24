"""Application services for video generation."""

DEMO_VIDEO_URL = "https://www.w3schools.com/html/mov_bbb.mp4"


def generate_demo_video(prompt: str) -> str:
    """Return a sample video URL until an AI model is integrated.

    The prompt parameter is intentionally accepted here so this function can be
    replaced by a real inference service without changing the API endpoint.
    """

    _ = prompt
    return DEMO_VIDEO_URL
