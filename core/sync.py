from .database_fb import get_fb_connection
from .database_pg import get_pg_connection

def sincronizar_logistica():
    fb_conn = get_fb_connection()
    pg_conn = get_pg_connection()
    
    if not fb_conn or not pg_conn:
        return

    try:
        fb_cur = fb_conn.cursor()
        pg_cur = pg_conn.cursor()

        # 1. Extração do Firebird
        print("Lendo dados do Firebird...")
        fb_cur.execute("SELECT ID, RASTREIO, CLIENTE, DATA FROM TABELA_FRETE")
        rows = fb_cur.fetchall()

        # 2. Carga no Postgres (Usando UPSERT para não duplicar)
        print(f"Sincronizando {len(rows)} registros no Postgres...")
        insert_query = """
            INSERT INTO entregas (id_origem_fb, codigo_rastreio, cliente_nome, data_saida)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id_origem_fb) DO UPDATE SET
                codigo_rastreio = EXCLUDED.codigo_rastreio,
                cliente_nome = EXCLUDED.cliente_nome,
                status_atual = 'SINCRONIZADO';
        """
        
        # Executemany é eficiente para SQL Puro
        pg_cur.executemany(insert_query, rows)
        
        pg_conn.commit()
        print("Sincronização finalizada com sucesso!")

    except Exception as e:
        print(f"Erro durante a sincronização: {e}")
        pg_conn.rollback()
    finally:
        fb_conn.close()
        pg_conn.close()

if __name__ == "__main__":
    sincronizar_logistica()