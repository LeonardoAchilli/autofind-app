2_🔑_Admin.py (Pagina Admin)
L'area riservata per visualizzare e gestire le richieste.

import streamlit as st
import pandas as pd
from core.database import get_all_requests, update_request_status
from core.utils import check_password

st.set_page_config(page_title="Area Admin", page_icon="🔑", layout="wide")

st.title("🔑 Area Amministrativa")

# Controlla la password prima di mostrare qualsiasi contenuto
if not check_password():
    st.stop() # Ferma l'esecuzione se la password non è corretta

st.success("Accesso effettuato con successo.")
st.markdown("### Storico Richieste Clienti")

# Recupera i dati
requests_df = get_all_requests()

if requests_df.empty:
    st.info("Nessuna richiesta trovata nel database.")
else:
    # Mostra la tabella con tutte le richieste
    st.dataframe(requests_df, use_container_width=True)

    st.markdown("---")
    st.subheader("Gestisci Richiesta")

    # Seleziona una richiesta da modificare
    col1, col2 = st.columns(2)
    with col1:
        request_id_to_update = st.number_input(
            "Inserisci l'ID della richiesta da aggiornare",
            min_value=1,
            step=1,
            value=None
        )
    with col2:
        # Definisci gli stati possibili
        status_options = ["Nuova", "In Lavorazione", "Contattato", "Completata", "Annullata"]
        new_status = st.selectbox(
            "Seleziona il nuovo stato",
            options=status_options,
            index=None
        )

    if st.button("Aggiorna Stato"):
        if request_id_to_update and new_status:
            if update_request_status(request_id_to_update, new_status):
                st.success(f"Stato della richiesta #{request_id_to_update} aggiornato a '{new_status}'.")
                st.rerun() # Ricarica la pagina per mostrare i dati aggiornati
            else:
                st.error("Errore durante l'aggiornamento.")
        else:
            st.warning("Per favore, inserisci un ID e seleziona un nuovo stato.")
