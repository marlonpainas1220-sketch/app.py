import streamlit as st
from openai import OpenAI
import os

# 1. Configuração inicial (DEVE ser a primeira linha de comando Streamlit)
st.set_page_config(page_title="IA Star Studio", layout="wide")

# 2. Busca a chave nos Secrets do Streamlit
try:
    api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=api_key)
except Exception:
    st.error("❌ Erro: Chave 'OPENAI_API_KEY' não encontrada nos Secrets do Streamlit.")
    st.stop()

# 3. Interface Visual
st.title("🎤 AI Content Studio")

with st.sidebar:
    st.header("🧬 DNA da Modelo")
    cabelo = st.text_input("Cabelo", "Rosa pastel")
    rosto = st.text_input("Rosto", "Olhos verdes")
    st.divider()
    gerar = st.button("🚀 PRODUZIR AGORA")

briefing = st.text_area("O que ela está fazendo?", placeholder="Ex: No palco de um show...")

if gerar:
    if not briefing:
        st.warning("Descreva a cena.")
    else:
        with st.spinner("✨ Criando..."):
            try:
                # Gerar Imagem
                prompt_f = f"Photo of a woman, {cabelo}, {rosto}. Action: {briefing}. 8k, realistic."
                img_resp = client.images.generate(model="dall-e-3", prompt=prompt_f)
                st.image(img_resp.data[0].url)
                
                # Gerar Texto
                txt_resp = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": f"Legenda para: {briefing}"}]
                )
                st.success(txt_resp.choices[0].message.content)
            except Exception as e:
                st.error(f"Erro na Produção: {e}")
