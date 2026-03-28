import fdb

# Configurações do Firebird (Fonte de Dados)
FB_CONF = {
    'dsn': 'localhost:/caminho/para/seu/banco.fdb',
    'user': 'SYSDBA',
    'password': 'masterkey',
    'charset': 'WIN1252'
}

def get_fb_connection():
    try:
        conn = fdb.connect(**FB_CONF)
        return conn
    except Exception as e:
        print(f"Erro ao conectar no Firebird: {e}")
        return None