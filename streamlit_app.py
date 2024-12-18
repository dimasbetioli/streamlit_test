import streamlit as st

st.set_page_config(
    page_title="Teste de Tema",
    page_icon="https://raw.githubusercontent.com/dimasbetioli/streamlit_test/refs/heads/main/mult.png",
    layout="centered"
)

primaryColor = "#ff0000"  # Vermelho
backgroundColor = "#000000"  # Preto
secondaryBackgroundColor = "#1e1e1e"  # Cinza escuro
textColor = "#ffffff"  # Branco
font = "monospace"  # Altere para uma fonte diferente

st.sidebar.divider()
c1,c2 = st.sidebar.columns([2,2])

logo1 = "https://raw.githubusercontent.com/dimasbetioli/streamlit_test/refs/heads/main/logo1.png"
logo2 = "https://raw.githubusercontent.com/dimasbetioli/streamlit_test/refs/heads/main/logo2.png"

c1.image(logo1)
c2.image(logo2)

st.title("🎉 Aplicação Simples com Streamlit")
st.write("Este é um teste para aplicar temas com `config.toml`.")

# Entrada simples
nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Olá, {nome}! O tema está funcionando? 😊")
