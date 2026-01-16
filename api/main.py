from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import edge_tts
import asyncio
from gradio_client import Client, handle_file
import uuid

app = FastAPI()

# Blindagem contra erros de domínio (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/generate")
async def generate(data: dict):
    try:
        prompt = data.get("prompt")
        mode = data.get("mode")
        
        # Gerador de Voz Grátis
        voice_file = f"/tmp/{uuid.uuid4()}.mp3"
        communicate = edge_tts.Communicate(prompt, "pt-BR-FranciscaNeural")
        await communicate.save(voice_file)

        # Integração com LivePortrait (Fisionomia Fixa)
        if mode == "video":
            client = Client("Kwai-VGI/LivePortrait")
            result = client.predict(
                input_image=handle_file(data.get("face_url")),
                input_video=handle_file("https://github.com/marlonpainas1220-sketch/Gerado-02-/raw/main/ref.mp4"),
                api_name="/predict"
            )
            return {"status": "success", "url": result}
            
        return {"status": "success", "audio": voice_file}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
