import sqlite3
import pandas as pd
from pathlib import Path

# Definiamo il percorso del file di database all'interno della cartella 'data'
DB_FILE = Path(__file__).parent.parent / "data" / "autofind.db"
DB_FILE.parent.mkdir(parents=True, exist_ok=True) # Crea la cartella 'data' se non esiste

def get_connection():
    """Crea e restituisce una connessione al database."""
    return sqlite3.connect(DB_FILE)

def init_db():
    """Inizializza il database creando la tabella delle richieste se non esiste."""
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                nome TEXT NOT NULL,
                cognome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefono TEXT,
                marca TEXT NOT NULL,
                modello TEXT NOT NULL,
                anno_min INTEGER,
                budget REAL,
                note TEXT,
                status TEXT NOT NULL
            )
        """)
        con.commit()
    except sqlite3.Error as e:
        print(f"Errore durante l'inizializzazione del DB: {e}")
    finally:
        if con:
            con.close()

def add_request(data):
    """Aggiunge una nuova richiesta al database."""
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO requests (timestamp, nome, cognome, email, telefono, marca, modello, anno_min, budget, note, status)
            VALUES (datetime('now', 'localtime'), ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Nuova')
        """, tuple(data.values()))
        con.commit()
    except sqlite3.Error as e:
        print(f"Errore durante l'aggiunta della richiesta: {e}")
        return False
    finally:
        if con:
            con.close()
    return True

def get_all_requests():
    """Recupera tutte le richieste dal database e le restituisce come DataFrame pandas."""
    try:
        con = get_connection()
        # Usiamo pandas per leggere direttamente la query SQL in un DataFrame
        df = pd.read_sql_query("SELECT * FROM requests ORDER BY id DESC", con)
        return df
    except (sqlite3.Error, pd.errors.DatabaseError) as e:
        print(f"Errore nel recuperare le richieste: {e}")
        return pd.DataFrame() # Restituisce un DataFrame vuoto in caso di errore
    finally:
        if 'con' in locals() and con:
            con.close()

def update_request_status(request_id, new_status):
    """Aggiorna lo stato di una specifica richiesta."""
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("UPDATE requests SET status = ? WHERE id = ?", (new_status, request_id))
        con.commit()
    except sqlite3.Error as e:
        print(f"Errore durante l'aggiornamento dello stato: {e}")
        return False
    finally:
        if con:
            con.close()
    return True
