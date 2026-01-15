import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis de ambiente
load_dotenv()

# Cria o cliente OpenAI apenas se a chave estiver configurada
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

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
    if client:
        try:
            prompt = f"""
            Crie um roteiro de conteúdo para redes sociais com as seguintes características:
            
            Tema: {tema}
            Estilo: {perfil.get('estilo', 'N/A')}
            Tom de Voz: {perfil.get('voz', 'N/A')}
            Ritmo: {perfil.get('ritmo_corte', 'N/A')}
            
            O roteiro deve ter entre 30 a 60 segundos de duração e ser engajante.
            """
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um criador de conteúdo especializado em roteiros para redes sociais."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️ Erro ao chamar OpenAI API: {e}")
            print("💡 Usando modo simulação...")
            return "Conteúdo Gerado com Sucesso! Pronto para publicação. (Modo simulação - configure OPENAI_API_KEY para usar IA real)"
    else:
        print("ℹ️ OPENAI_API_KEY não configurada. Usando modo simulação.")
        return "Conteúdo Gerado com Sucesso! Pronto para publicação. (Modo simulação - configure OPENAI_API_KEY para usar IA real)"

# Fluxo principal
if __name__ == "__main__":
    videos_cliente = ["estetica.mp4", "voz.mp4", "ritmo.mp4"]
    perfil_extraido = processar_dna_influencer(videos_cliente)
    resultado = gerar_conteudo_autonomo("Tendências de Moda IA 2026", perfil_extraido)
    print(resultado)
