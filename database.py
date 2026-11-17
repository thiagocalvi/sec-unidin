import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "unidin.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def encripta_password(password):
    # Vulnerabilidade 10 - Hash com salt aleatório e fator de trabalho (werkzeug)
    return generate_password_hash(password)

def init_db():
    conn = get_connection()
    '''
        Essa função está intencionalmente 'vazia' para que você, caro(a) aluno(a), não veja o formato completo das tabelas, bem como ela está populada :)
    '''
    
    conn.close()
