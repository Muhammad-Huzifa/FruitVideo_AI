from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Input data structure
class VideoRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "FruitVideo AI Backend is Live! 🚀"}

@app.post("/generate")
def generate_video(request: VideoRequest):
    # Yahan aapka AI model logic aayega
    # Filhal hum sirf ek success message aur dummy URL bhej rahe hain
    prompt = request.prompt
    print(f"Generating video for prompt: {prompt}")
    
    return {
        "status": "success",
        "prompt": prompt,
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    }
