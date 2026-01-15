from flask import Flask, jsonify, request
import os

app = Flask(__name__)

def processar_dna_influencer(videos):
    """
    Analisa os vídeos de referência e extrai os metadados de estilo.
    """
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
    return "Conteúdo Gerado com Sucesso! Pronto para publicação."

@app.route('/')
def home():
    """
    Endpoint principal - retorna informações sobre o serviço
    """
    return jsonify({
        "status": "active",
        "service": "AI.PRODUTORA - DNA CONTENT ENGINE",
        "description": "Uma plataforma de produção de conteúdo autónomo para influenciadores gerados por Inteligência Artificial",
        "version": "1.0.0",
        "endpoints": {
            "/": "Informações do serviço",
            "/api/processar-dna": "POST - Processar DNA do influencer",
            "/api/gerar-conteudo": "POST - Gerar conteúdo autônomo"
        }
    })

@app.route('/api/processar-dna', methods=['POST'])
def processar_dna():
    """
    Endpoint para processar DNA do influencer
    
    Request body example:
    {
        "videos": ["estetica.mp4", "voz.mp4", "ritmo.mp4"]
    }
    """
    try:
        data = request.get_json(silent=False)
        if data is None:
            data = {}
        videos = data.get('videos', ["estetica.mp4", "voz.mp4", "ritmo.mp4"])
        perfil_extraido = processar_dna_influencer(videos)
        return jsonify({
            "status": "success",
            "perfil": perfil_extraido
        })
    except Exception:
        return jsonify({
            "status": "error",
            "message": "Erro ao processar DNA do influencer. Por favor, verifique os dados enviados."
        }), 500

@app.route('/api/gerar-conteudo', methods=['POST'])
def gerar_conteudo():
    """
    Endpoint para gerar conteúdo autônomo
    
    Request body example:
    {
        "tema": "Tendências de Moda IA 2026",
        "perfil": {
            "estilo": "High-Energy / Futurista",
            "voz": "Frequência média, sotaque neutro",
            "ritmo_corte": "1.2 segundos por transição"
        }
    }
    """
    try:
        data = request.get_json(silent=False)
        if data is None:
            data = {}
        tema = data.get('tema', 'Tendências de Moda IA 2026')
        perfil = data.get('perfil', {
            "estilo": "High-Energy / Futurista",
            "voz": "Frequência média, sotaque neutro",
            "ritmo_corte": "1.2 segundos por transição"
        })
        resultado = gerar_conteudo_autonomo(tema, perfil)
        return jsonify({
            "status": "success",
            "resultado": resultado,
            "tema": tema,
            "perfil": perfil
        })
    except Exception:
        return jsonify({
            "status": "error",
            "message": "Erro ao gerar conteúdo. Por favor, verifique os dados enviados."
        }), 500

# Handler para Vercel - expõe o app Flask
# Vercel procura por esta variável para executar a aplicação
handler = app

# Fluxo principal para teste local
if __name__ == "__main__":
    # Debug mode only for local development
    # In production (Vercel), the app runs without this block
    import sys
    debug_mode = '--debug' in sys.argv
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
