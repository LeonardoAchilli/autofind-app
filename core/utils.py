import streamlit as st

def check_password():
    """Restituisce True se l'utente ha inserito la password corretta, altrimenti False."""
    try:
        # La password corretta è memorizzata negli secrets di Streamlit
        correct_password = st.secrets["admin"]["password"]
    except (KeyError, AttributeError):
        st.error("La configurazione della password non è presente negli secrets di Streamlit.")
        st.info("Contatta l'amministratore per configurare il file `secrets.toml` per lo sviluppo locale o i secrets in Streamlit Cloud.")
        return False

    # Chiede all'utente di inserire la password
    password = st.text_input("Inserisci la password per accedere:", type="password")

    if not password:
        st.stop() # Ferma l'esecuzione se non è stata inserita nessuna password

    if password == correct_password:
        return True
    else:
        st.error("Password errata.")
        return False
