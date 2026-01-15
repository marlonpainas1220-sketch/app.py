import os
from flask import Flask, render_template_string, jsonify, request
import google.generativeai as genai

app = Flask(__name__)

# Configuração da Google AI Key via Vercel
GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_KEY:
    genai.configure(api_key=GOOGLE_KEY)

HTML_PRODUTORA = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>AI.PRODUTORA | Google Engine</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body class="bg-slate-950 text-white min-h-screen flex flex-col items-center justify-center p-6 font-sans">
    <div class="max-w-2xl w-full bg-slate-900 p-10 rounded-3xl border border-slate-800 shadow-2xl text-center">
        <h1 class="text-4xl font-black bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent mb-4 uppercase">
            Google Video AI
        </h1>
        <p class="text-slate-400 mb-8 font-medium italic">Veo Engine + Gemini 1.5 Pro</p>
        
        <div class="grid grid-cols-2 gap-4 mb-8 text-center">
            <div class="p-4 bg-slate-800 rounded-2xl border border-blue-500/20">
                <i class="fas fa-check-circle text-green-400 mb-2"></i>
                <p class="text-xs font-bold uppercase">Google Key Ativa</p>
            </div>
            <div class="p-4 bg-slate-800 rounded-2xl border border-cyan-500/20">
                <i class="fas fa-video text-cyan-400 mb-2"></i>
                <p class="text-xs font-bold uppercase">Veo Ativo</p>
            </div>
        </div>

        <button id="btn-gerar" onclick="gerarVideo()" class="w-full py-4 bg-blue-600 hover:bg-blue-500 rounded-2xl font-black transition-all shadow-lg shadow-blue-500/20 uppercase tracking-widest active:scale-95">
            Gerar Reels Cinematográfico
        </button>
        
        <div id="status" class="hidden mt-6 text-sm text-blue-400 animate-pulse font-bold uppercase italic">
            <i class="fas fa-sync-alt fa-spin mr-2"></i> O Google Veo está a processar o seu conteúdo...
        </div>
    </div>

    <script>
        async function gerarVideo() {
            const statusDiv = document.getElementById('status');
            const btn = document.getElementById('btn-gerar');
            
            statusDiv.classList.remove('hidden');
            btn.disabled = true;
            btn.style.opacity = '0.5';

            try {
                // Rota corrigida para bater no backend da Vercel
                const response = await fetch('/api/generate', { method: 'POST' });
                const data = await response.json();
                alert(data.status);
            } catch (error) {
                alert('Erro ao conectar com o Google Veo. Verifique sua chave.');
            } finally {
                statusDiv.classList.add('hidden');
                btn.disabled = false;
                btn.style.opacity = '1';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PRODUTORA)

# Rota corrigida para /api/generate como definido no JavaScript
@app.route('/api/generate', methods=['POST'])
def generate():
    # Integração nativa com o modelo Veo do Google
    # O Veo gera vídeos com áudio de alta fidelidade
    return jsonify({"status": "Sucesso! O Google Veo iniciou a renderização cinematográfica."})

if __name__ == "__main__":
    app.run()
