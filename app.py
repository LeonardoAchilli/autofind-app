import streamlit as st
from core.database import init_db

# Inizializza il database alla prima esecuzione
init_db()

# Configurazione della pagina
st.set_page_config(
    page_title="AutoFind - Trova la tua auto",
    page_icon="🔎",
    layout="wide"
)

# --- Contenuto della Pagina ---
st.title("Benvenuto in AutoFind 🔎")
st.markdown("### Il servizio che trova l'auto dei tuoi sogni per te.")

st.write("")  # Spazio

col1, col2 = st.columns([1, 1])

with col1:
    st.image("https://placehold.co/600x400/000000/FFFFFF?text=Immagine+di+un'auto", 
             use_container_width=True, 
             caption="La tua prossima auto ti sta aspettando")

with col2:
    st.write(
        """
        **Sei stanco di passare ore sui siti di annunci senza trovare l'auto giusta?**
        
        AutoFind semplifica il processo. Dimentica lo stress della ricerca: dicci cosa cerchi e noi la troveremo per te.
        
        #### Come funziona?
        1. **Vai alla pagina "Cerca Auto"**: Usa il menu a sinistra per navigare.
        2. **Compila il modulo**: Inserisci i dettagli dell'auto che desideri (marca, modello, budget, etc.).
        3. **Invia la tua richiesta**: Il nostro team si metterà subito al lavoro.
        4. **Rilassati**: Ti contatteremo noi non appena avremo trovato le opzioni migliori che corrispondono ai tuoi criteri.
        
        **Inizia ora! Clicca su `🚗 Cerca Auto` nel menu a sinistra.**
        """
    )

st.info("Sei un amministratore? Accedi alla tua area riservata dal menu `🔑 Admin`.")
