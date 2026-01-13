import streamlit as st
from openai import OpenAI
import os

# --- ACESSO SEGURO À API ---
# A Vercel injeta a chave automaticamente aqui
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="IA Star Studio", layout="wide")

# Estilo Visual Dark/Neon
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .stButton>button { 
        background: linear-gradient(90deg, #ff00cc, #3333ff); 
        color: white; border: none; border-radius: 12px; font-weight: bold; height: 3em;
    }
    </style>
""", unsafe_allow_html=True)

# BARRA LATERAL - DNA DA MODELO
with st.sidebar:
    st.header("🧬 DNA da Modelo")
    cabelo = st.text_input("Cabelo", "Curto liso azul neon")
    rosto = st.text_input("Rosto", "Olhos puxados, traços finos")
    estilo = st.text_input("Estilo", "Popstar urbana")
    st.divider()
    personalidade = st.selectbox("Personalidade", ["Debochada", "Meiga", "Empoderada"])

# ÁREA CENTRAL
st.title("🎤 AI Content Studio")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 O que ela está fazendo?")
    briefing = st.text_area("Descreva a cena:", placeholder="Ex: Gravando um clipe no topo de um prédio...")
    gerar = st.button("🚀 PRODUZIR CONTEÚDO")

with col2:
    if gerar:
        if not api_key:
            st.error("Erro: A chave 'OPENAI_API_KEY' não foi encontrada na Vercel.")
        elif not briefing:
            st.warning("Descreva a cena primeiro.")
        else:
            with st.spinner("✨ Criando foto e legenda..."):
                try:
                    # Geração de Imagem
                    prompt = f"Professional photo of a woman with {cabelo}, {rosto}, style {estilo}. Action: {briefing}. 8k resolution, cinematic lighting."
                    img_resp = client.images.generate(model="dall-e-3", prompt=prompt)
                    st.image(img_resp.data[0].url, use_column_width=True)
                    
                    # Geração de Legenda
                    txt_resp = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": f"Crie uma legenda para Instagram de uma IA influencer {personalidade} fazendo isso: {briefing}. Use emojis."}]
                    )
                    st.success("Legenda Sugerida:")
                    st.write(txt_resp.choices[0].message.content)
                except Exception as e:
                    st.error(f"Erro na API: {e}")
