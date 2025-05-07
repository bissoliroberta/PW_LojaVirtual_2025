CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS clientes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
CPF TEXT NOT NULL,
email TEXT NOT NULL,
telefone TEXT NOT NULL,
senha TEXT NOT NULL)
"""

INSERIR_CLIENTE = """
INSERT INTO clientes (nome, CPF, email, telefone, senha) 
VALUES (?, ?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
id, nome, CPF, email, telefone, senha 
FROM clientes
""" 