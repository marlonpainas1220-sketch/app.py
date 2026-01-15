import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Cria o cliente OpenAI apenas se a chave estiver configurada
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

def exemplo_openai_chat():
    """
    Exemplo de uso da API OpenAI usando o modelo Chat (recomendado para GPT-3.5/GPT-4).
    """
    if not client:
        print("⚠️ Cliente OpenAI não inicializado. Configure OPENAI_API_KEY.")
        return None
        
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil especializado em integração de APIs."},
                {"role": "user", "content": "Escreva um exemplo de integração com a API OpenAI."}
            ],
            max_tokens=150
        )
        print("\n=== Exemplo de Chat Completion ===")
        print(response.choices[0].message.content.strip())
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Erro ao chamar API OpenAI (Chat): {e}")
        return None

def gerar_roteiro_com_openai(tema, perfil):
    """
    Gera um roteiro de conteúdo usando OpenAI baseado no tema e perfil.
    """
    if not client:
        print("⚠️ Cliente OpenAI não inicializado. Configure OPENAI_API_KEY.")
        return None
        
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
        
        roteiro = response.choices[0].message.content.strip()
        print("\n=== Roteiro Gerado ===")
        print(roteiro)
        return roteiro
    except Exception as e:
        print(f"Erro ao gerar roteiro: {e}")
        return None

# Fluxo principal de demonstração
if __name__ == "__main__":
    print("🚀 Testando Integração OpenAI API\n")
    
    # Verifica se a chave de API está configurada
    if not api_key or api_key == "your_openai_api_key_here":
        print("⚠️ ERRO: Configure sua OPENAI_API_KEY no arquivo .env")
        print("Copie o arquivo .env.example para .env e adicione sua chave de API.")
    else:
        print("✓ Chave de API OpenAI configurada\n")
        
        # Exemplo: Chat Completion (recomendado)
        exemplo_openai_chat()
        
        # Exemplo: Geração de roteiro personalizado
        perfil_exemplo = {
            "estilo": "High-Energy / Futurista",
            "voz": "Frequência média, sotaque neutro",
            "ritmo_corte": "1.2 segundos por transição"
        }
        gerar_roteiro_com_openai("Tendências de Moda IA 2026", perfil_exemplo)
