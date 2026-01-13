import streamlit as st
from openai import OpenAI
import os

# --- CONFIGURAÇÃO DE SEGURANÇA ---
# O código busca a chave nas "Secrets" (TOML) ou Variáveis de Ambiente
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# --- LAYOUT DO APP ---
st.set_page_config(
    page_title="AI Star Studio",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Neon Dark
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stButton>button {
        background: linear-gradient(90deg, #ff00cc, #3333ff);
        color: white; border: none; border-radius: 12px;
        font-weight: bold; height: 3.5em; width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 15px rgba(255, 0, 204, 0.4); }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL: O DNA DA MODELO ---
with st.sidebar:
    st.title("🧬 DNA da Star")
    st.subheader("Configurações Fixas")
    
    # Estes campos mantêm a consistência visual
    modelo_base = st.text_input("Nome da Modelo", "Luna AI")
    cabelo = st.text_input("Cabelo", "Curto, azul neon, corte bob")
    rosto = st.text_input("Rosto", "Traços finos, olhos verdes, pele clara")
    estilo = st.text_input("Estilo Padrão", "Cyberpunk Popstar")
    
    st.divider()
    personalidade = st.selectbox("Voz da Persona", ["Debochada", "Meiga", "Empoderada", "Misteriosa"])
    st.caption("A IA usará esses dados para manter o rosto sempre igual.")

# --- PAINEL PRINCIPAL ---
st.title("🎤 AI Content Studio")
st.write(f"Produzindo conteúdo para **{modelo_base}**")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Briefing da Cena")
    briefing = st.text_area(
        "O que ela está fazendo agora?", 
        placeholder="Ex: Saindo de um show lotado em Tokyo com luzes neon ao fundo...",
        height=180
    )
    
    formato = st.multiselect(
        "O que você quer gerar?",
        ["Post para Feed", "Story de Texto", "Roteiro de Reels"],
        default=["Post para Feed"]
    )
    
    gerar = st.button("🚀 INICIAR PRODUÇÃO")

with col2:
    if gerar:
        if not api_key:
            st.error("Chave API não configurada! Verifique suas Secrets ou Env Vars.")
        elif not briefing:
            st.warning("Por favor, descreva a cena para a IA.")
        else:
            with st.spinner("✨ A IA está criando a mídia e os textos..."):
                try:
                    # 1. Geração da Imagem com DALL-E 3
                    # O segredo da consistência é somar o DNA ao Briefing
                    prompt_visual = (
                        f"Photorealistic 8k studio photography of a famous female popstar, "
                        f"{cabelo}, {rosto}, wearing {estilo} outfit. "
                        f"Scene: {briefing}. Cinematic lighting, professional editing, "
                        f"highly detailed face, consistent facial features."
                    )
                    
                    img_response = client.images.generate(
                        model="dall-e-3",
                        prompt=prompt_visual,
                        n=1,
                        size="1024x1024",
                        quality="hd"
                    )
                    
                    st.image(img_response.data[0].url, caption="Publicação Sugerida", use_container_width=True)

                    # 2. Geração dos Textos com GPT-4o
                    prompt_texto = (
                        f"Você é a social media da {modelo_base}, uma influencer de IA {personalidade}. "
                        f"Crie conteúdo para {formato} baseado na cena: {briefing}. "
                        f"Use gírias de 2026, emojis e chame os seguidores de 'Nebulosos'."
                    )
                    
                    text_response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": prompt_texto}]
                    )
                    
                    st.success("Produção Finalizada!")
                    st.markdown("### ✍️ Copywriting")
                    st.write(text_response.choices[0].message.content)
                    
                except Exception as e:
                    st.error(f"Ocorreu um erro técnico: {str(e)}")
    else:
        st.info("Preencha o briefing ao lado para começar a mágica.")

st.divider()
st.caption("© 2026 AI Influencer Studio - Gerenciamento de Identidade Digital")
