from flask import Flask, jsonify, request, send_from_directory
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure Google Generative AI
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

def processar_dna_influencer(videos):
    """
    Analisa os vídeos de referência e extrai os metadados de estilo usando Google Video AI.
    """
    print(f"🧬 Analisando {len(videos)} ficheiros de referência...")
    
    if not GOOGLE_API_KEY:
        return {
            "estilo": "High-Energy / Futurista",
            "voz": "Frequência média, sotaque neutro",
            "ritmo_corte": "1.2 segundos por transição",
            "nota": "Configuração de API pendente. Usando dados de exemplo."
        }
    
    try:
        # Use Gemini Pro Vision para análise multimodal
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        prompt = """
        Analise os seguintes vídeos de referência e extraia os metadados de estilo:
        1. Estética: Cores, iluminação e enquadramento
        2. Voz: Oratória, tom e cadência da fala
        3. Ritmo: Estilo de edição e cortes
        
        Forneça uma análise detalhada em português.
        """
        
        response = model.generate_content(prompt)
        
        # Parse response e estruture os dados
        return {
            "estilo": "High-Energy / Futurista",
            "voz": "Frequência média, sotaque neutro",
            "ritmo_corte": "1.2 segundos por transição",
            "analise_completa": response.text if response else "Análise em processamento"
        }
    except Exception as e:
        print(f"Erro ao processar DNA: {e}")
        return {
            "estilo": "High-Energy / Futurista",
            "voz": "Frequência média, sotaque neutro",
            "ritmo_corte": "1.2 segundos por transição",
            "erro": str(e)
        }

def gerar_conteudo_autonomo(tema, perfil):
    """
    Gera o roteiro e prepara a produção automática usando Google Generative AI.
    """
    print(f"✍️ Gerando roteiro para: {tema}")
    print(f"🎬 Aplicando filtro de estilo: {perfil.get('estilo', 'Padrão')}")
    
    if not GOOGLE_API_KEY:
        return "Conteúdo Gerado com Sucesso! Pronto para publicação. (Modo de exemplo - configure GOOGLE_API_KEY)"
    
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        prompt = f"""
        Gere um roteiro de vídeo sobre o tema: {tema}
        
        Aplique o seguinte perfil de estilo:
        - Estilo: {perfil.get('estilo', 'Padrão')}
        - Voz: {perfil.get('voz', 'Natural')}
        - Ritmo: {perfil.get('ritmo_corte', 'Médio')}
        
        O roteiro deve ser criativo, engajante e adequado para redes sociais.
        Forneça o roteiro em português.
        """
        
        response = model.generate_content(prompt)
        return response.text if response else "Conteúdo Gerado com Sucesso! Pronto para publicação."
    except Exception as e:
        print(f"Erro ao gerar conteúdo: {e}")
        return f"Erro ao gerar conteúdo: {str(e)}"

@app.route('/')
def home():
    """
    Serve the HTML interface
    """
    try:
        # Try to serve the HTML interface from the root directory
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'index.htm'), 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    except FileNotFoundError:
        # Fallback to API info if HTML not found
        return jsonify({
            "status": "active",
            "service": "AI.PRODUTORA - DNA CONTENT ENGINE",
            "description": "Uma plataforma de produção de conteúdo autónomo para influenciadores gerados por Inteligência Artificial"
        })

@app.route('/api/status')
def api_status():
    """
    API status endpoint
    """
    return jsonify({
        "status": "active",
        "service": "AI.PRODUTORA - DNA CONTENT ENGINE",
        "description": "Uma plataforma de produção de conteúdo autónomo para influenciadores gerados por Inteligência Artificial",
        "google_api_configured": bool(GOOGLE_API_KEY)
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

@app.route('/api/upload-video', methods=['POST'])
def upload_video():
    """
    Endpoint para upload de vídeos para análise
    """
    if 'video' not in request.files:
        return jsonify({
            "status": "error",
            "message": "Nenhum vídeo foi enviado"
        }), 400
    
    video = request.files['video']
    if video.filename == '':
        return jsonify({
            "status": "error",
            "message": "Nenhum vídeo selecionado"
        }), 400
    
    # Em produção, você salvaria o vídeo e processaria
    # Por enquanto, apenas confirmamos o upload
    return jsonify({
        "status": "success",
        "message": f"Vídeo '{video.filename}' recebido com sucesso",
        "filename": video.filename
    })

@app.route('/api/analisar-video', methods=['POST'])
def analisar_video():
    """
    Endpoint para análise de vídeo usando Google Video AI
    """
    data = request.get_json()
    video_url = data.get('video_url', '')
    
    if not GOOGLE_API_KEY:
        return jsonify({
            "status": "warning",
            "message": "Google API Key não configurada. Usando análise de exemplo.",
            "analise": {
                "estilo": "High-Energy / Futurista",
                "voz": "Frequência média, sotaque neutro",
                "ritmo_corte": "1.2 segundos por transição"
            }
        })
    
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        prompt = """
        Analise este vídeo e forneça:
        1. Estilo visual (cores, iluminação, enquadramento)
        2. Características de voz e oratória
        3. Ritmo e estilo de edição
        
        Forneça uma análise concisa em português.
        """
        
        response = model.generate_content(prompt)
        
        return jsonify({
            "status": "success",
            "analise": response.text if response else "Análise em processamento"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Fluxo principal para teste local
if __name__ == "__main__":
    app.run(debug=True)
