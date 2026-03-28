CREATE DATABASE sul_db;

-- Tabela de Entregas/Logística
CREATE TABLE IF NOT EXISTS entregas (
    id_sul SERIAL PRIMARY KEY,
    id_origem_fb INTEGER UNIQUE,       -- ID original do Firebird para evitar duplicidade
    codigo_rastreio VARCHAR(50) UNIQUE,
    cliente_nome VARCHAR(255),
    data_saida TIMESTAMP,
    status_atual VARCHAR(20) DEFAULT 'PENDENTE',
    ultima_sincronizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Logs (Útil para debugar a sincronização)
CREATE TABLE IF NOT EXISTS sync_logs (
    id SERIAL PRIMARY KEY,
    tabela_afetada VARCHAR(50),
    registros_processados INTEGER,
    data_execucao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status_resultado VARCHAR(20) -- 'SUCESSO' ou 'ERRO'
);