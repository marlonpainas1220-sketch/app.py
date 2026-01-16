from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# 1. TRAVA DE DOMÍNIO: Só aceita requisições do seu WordPress
ALLOWED_ORIGINS = [
    "https://seudominio.com",      # Seu site oficial
    "https://ia.seudominio.com",   # Seu subdomínio do app
    "http://localhost:3000"        # Para seus testes locais
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["POST"], # Só aceita envio de dados
    allow_headers=["*"],
)

# 2. TRAVA DE CHAVE: Função que valida a Secret Key
API_SECRET_KEY = "SUA_CHAVE_SUPER_SECRETA_AQUI" # Mude isto!

async def verify_token(x_api_key: str = Header(None)):
    if x_api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Acesso não autorizado.")
    return x_api_key

@app.post("/api/generate", dependencies=[Depends(verify_token)])
async def generate(data: dict):
    # O código de geração da IA continua aqui...
    return {"status": "success", "msg": "Processando com segurança"}
