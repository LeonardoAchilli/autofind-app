import streamlit as st
from core.database import add_request
import datetime

st.set_page_config(page_title="Invia Richiesta", page_icon="🚗")

st.title("🚗 Invia la tua Richiesta")
st.markdown("Compila i campi qui sotto per farci sapere quale auto stai cercando. Ti contatteremo al più presto!")

with st.form("request_form", clear_on_submit=True):
    st.subheader("I tuoi dati")
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome", key="nome")
    with col2:
        cognome = st.text_input("Cognome", key="cognome")
    
    col3, col4 = st.columns(2)
    with col3:
        email = st.text_input("Email*", key="email")
    with col4:
        telefono = st.text_input("Telefono (opzionale)", key="telefono")

    st.subheader("Dettagli dell'auto")
    col5, col6 = st.columns(2)
    with col5:
        marca = st.text_input("Marca*", key="marca")
    with col6:
        modello = st.text_input("Modello*", key="modello")

    col7, col8 = st.columns(2)
    with col7:
        current_year = datetime.date.today().year
        anno_min = st.number_input(
            "Anno minimo di produzione", 
            min_value=1950, 
            max_value=current_year, 
            value=current_year - 5, 
            step=1,
            key="anno"
        )
    with col8:
        budget = st.number_input(
            "Budget massimo (€)", 
            min_value=0.0, 
            step=500.0, 
            format="%.2f",
            key="budget"
        )

    note = st.text_area("Altre preferenze (es. colore, chilometraggio massimo, tipo di carburante...)", key="note")

    st.markdown("I campi con `*` sono obbligatori.")

    # Bottone di invio
    submitted = st.form_submit_button("Invia Richiesta")

    if submitted:
        # Validazione dei campi obbligatori
        if not nome or not cognome or not email or not marca or not modello:
            st.error("Per favore, compila tutti i campi obbligatori (*).")
        else:
            # Crea un dizionario con i dati del form
            request_data = {
                "nome": nome,
                "cognome": cognome,
                "email": email,
                "telefono": telefono,
                "marca": marca,
                "modello": modello,
                "anno_min": anno_min,
                "budget": budget,
                "note": note
            }
            # Aggiungi la richiesta al database
            if add_request(request_data):
                st.success("🎉 Richiesta inviata con successo! Ti contatteremo presto.")
            else:
                st.error("Si è verificato un errore durante l'invio. Riprova.")
