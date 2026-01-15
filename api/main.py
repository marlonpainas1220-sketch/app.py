from flask import Flask, jsonify, request
import os

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
    Gera o roteiro e prepara a produção automática.
    """
    print(f"✍️ Gerando roteiro para: {tema}")
    print(f"🎬 Aplicando filtro de estilo: {perfil['estilo']}")
    return "Conteúdo Gerado com Sucesso! Pronto para publicação."

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
    Endpoint para gerar conteúdo autónomo
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
    app.run(debug=False)
