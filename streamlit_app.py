import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="App Atrativo",
    page_icon="🎨",
    layout="wide",  # Layout mais amplo para aproveitar o espaço
    initial_sidebar_state="expanded"
)

# Estilo da sidebar
with st.sidebar:
    st.image(
        "https://raw.githubusercontent.com/dimasbetioli/streamlit_test/refs/heads/main/mult.png",
        use_container_width=True,  # Corrigido para evitar o aviso
    )
    st.markdown(
        "<h2 style='text-align: center; color: #4CAF50;'>Menu</h2>",
        unsafe_allow_html=True,
    )
    st.divider()

    # Colunas para logos
    c1, c2 = st.columns(2)
    c1.image("https://raw.githubusercontent.com/dimasbetioli/streamlit_test/refs/heads/main/logo1.png", use_container_width=True)
    c2.image("https://raw.githubusercontent.com/dimasbetioli/streamlit_test/refs/heads/main/logo2.png", use_container_width=True)

# Título principal com emoji
st.markdown(
    "<h1 style='text-align: center; color: #2196F3;'>🎉 Aplicação Simples com Estilo</h1>",
    unsafe_allow_html=True,
)

# Caixa de introdução
st.markdown(
    """
    <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin: 10px 0;">
        <h3 style="text-align: center; color: #FF5722;">Este é um teste para personalizar o tema diretamente no código!</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Entrada de texto
nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Olá, {nome}! O tema está funcionando? 😊")

# Adicionando uma imagem como banner
st.image(
    "https://via.placeholder.com/1200x300.png?text=Bem-vindo+ao+App+Atrativo+com+Streamlit",
    caption="Personalização de layout no Streamlit",
    use_container_width=True,  # Corrigido para evitar o aviso
)

# Footer
st.markdown(
    """
    <footer style="text-align: center; margin-top: 20px;">
        <small>Feito com ❤️ usando Streamlit</small>
    </footer>
    """,
    unsafe_allow_html=True,
)
