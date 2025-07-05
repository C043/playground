from fastapi import APIRouter
from controllers import tts_controller
from models.tts_model import TTSRequest
from fastapi.responses import FileResponse

router = APIRouter()


@router.post("/speak")
async def speak_text(req: TTSRequest):
    path = await tts_controller.speak(req.text)
    return FileResponse(path, media_type="audio/mpeg", filename="output.mp3")
