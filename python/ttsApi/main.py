from fastapi import FastAPI, WebSocket
from routers import tts_routes
import subprocess
import uuid
from pathlib import Path
import json

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            json_data = json.loads(data)
            text = json_data["text"]

            file_path = Path(f"/tmp/{uuid.uuid4()}.mp3")

            subprocess.run(
                [
                    "edge-tts",
                    "--rate=+25%",
                    "--text",
                    text,
                    "--write-media",
                    str(file_path),
                ]
            )

            with open(file_path, "rb") as f:
                await websocket.send_bytes(f.read())

            file_path.unlink()
        except Exception as err:
            await websocket.send_text(f"Error: {str(err)}")
            break


app.include_router(tts_routes.router)
