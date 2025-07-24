import streamlit as st

# Imposta la configurazione della pagina.
# Questa configurazione è globale e viene applicata a tutte le pagine dell'app.
st.set_page_config(
    page_title="AutoFind",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Questo file principale può essere utilizzato per elementi comuni
# come un titolo nella sidebar o un footer.
st.sidebar.title("Navigazione")
st.sidebar.success("Seleziona una pagina qui sopra.")

# Aggiungiamo un po' di stile per migliorare l'aspetto
st.markdown("""
<style>
   .st-emotion-cache-16txtl3 {
        padding-top: 2rem;
    }
   .st-emotion-cache-1y4p8pa {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)