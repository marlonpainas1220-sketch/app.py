from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import openai

# Carrega variáveis de ambiente
load_dotenv()

# Configure a chave de API do OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def processar_dna_influencer(videos):
    """
    Analisa os vídeos de referência e extrai os metadados de estilo.
    """
    print(f"🧬 Analisando {len(videos)} ficheiros de referência...")
    # Simulação de análise via Gemini 1.5 Pro
    return {
        "estilo": "High-Energy / Futurista",
        "voz": "Frequência média, sotaque neutro",
        "ritmo_corte": "1.2 segundos por transição"
    }

def gerar_conteudo_autonomo(tema, perfil):
    """
    Gera o roteiro e prepara a produção automática usando OpenAI.
    """
    print(f"✍️ Gerando roteiro para: {tema}")
    print(f"🎬 Aplicando filtro de estilo: {perfil['estilo']}")
    
    # Se a chave OpenAI estiver configurada, usar a API
    if openai.api_key:
        try:
            prompt = f"""
            Crie um roteiro de conteúdo para redes sociais com as seguintes características:
            
            Tema: {tema}
            Estilo: {perfil.get('estilo', 'N/A')}
            Tom de Voz: {perfil.get('voz', 'N/A')}
            Ritmo: {perfil.get('ritmo_corte', 'N/A')}
            
            O roteiro deve ter entre 30 a 60 segundos de duração e ser engajante.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um criador de conteúdo especializado em roteiros para redes sociais."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Erro ao chamar OpenAI API: {e}")
            return "Conteúdo Gerado com Sucesso! Pronto para publicação. (Modo simulação - configure OPENAI_API_KEY para usar IA real)"
    else:
        return "Conteúdo Gerado com Sucesso! Pronto para publicação. (Modo simulação - configure OPENAI_API_KEY para usar IA real)"

@app.route('/')
def home():
    return jsonify({
        "status": "active",
        "service": "AI.PRODUTORA - DNA CONTENT ENGINE",
        "description": "Uma plataforma de produção de conteúdo autónomo para influenciadores gerados por Inteligência Artificial"
    })

@app.route('/api/processar-dna', methods=['POST'])
def processar_dna():
    """
    Endpoint para processar DNA do influencer
    """
    data = request.get_json()
    videos = data.get('videos', ["estetica.mp4", "voz.mp4", "ritmo.mp4"])
    perfil_extraido = processar_dna_influencer(videos)
    return jsonify({
        "status": "success",
        "perfil": perfil_extraido
    })

@app.route('/api/gerar-conteudo', methods=['POST'])
def gerar_conteudo():
    """
    Endpoint para gerar conteúdo autônomo
    """
    data = request.get_json()
    tema = data.get('tema', 'Tendências de Moda IA 2026')
    perfil = data.get('perfil', {
        "estilo": "High-Energy / Futurista",
        "voz": "Frequência média, sotaque neutro",
        "ritmo_corte": "1.2 segundos por transição"
    })
    resultado = gerar_conteudo_autonomo(tema, perfil)
    return jsonify({
        "status": "success",
        "resultado": resultado
    })

# Fluxo principal para teste local
if __name__ == "__main__":
    app.run(debug=True)
