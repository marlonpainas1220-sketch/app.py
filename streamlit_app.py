import streamlit as st
from openai import OpenAI

# 1. Configuração de Página (Sempre no topo)
st.set_page_config(page_title="IA Influencer Studio", layout="wide")

# 2. Conexão com a Chave dos Secrets
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception as e:
    st.error("Erro na chave! Verifique os Secrets no painel do Streamlit.")
    st.stop()

# 3. Interface do App
st.title("🎤 Estúdio da Cantora IA")

with st.sidebar:
    st.header("🧬 DNA Visual")
    cabelo = st.text_input("Cabelo", "Longo e Rosa")
    rosto = st.text_input("Rosto", "Traços finos, olhos verdes")
    st.divider()
    botao = st.button("🚀 GERAR POST")

cena = st.text_area("O que ela está fazendo?", "Gravando um clipe no estúdio")

if botao:
    with st.spinner("Criando..."):
        try:
            # Gerar Imagem
            prompt = f"Professional photo of a woman, {cabelo}, {rosto}. Action: {cena}. 8k photorealistic."
            res_img = client.images.generate(model="dall-e-3", prompt=prompt)
            st.image(res_img.data[0].url)
            
            # Gerar Texto
            res_txt = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": f"Legenda curta para Instagram sobre: {cena}"}]
            )
            st.success(res_txt.choices[0].message.content)
        except Exception as e:
            st.error(f"Erro: {e}")
