import streamlit as st

st.set_page_config(
    page_title="Teste de Tema",
    page_icon="🎨",
    layout="centered"
)

st.title("🎉 Aplicação Simples com Streamlit")
st.write("Este é um teste para aplicar temas com `config.toml`.")

# Entrada simples
nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Olá, {nome}! O tema está funcionando? 😊")
