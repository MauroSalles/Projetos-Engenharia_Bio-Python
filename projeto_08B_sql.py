import sqlite3

# 1. Conectando ao banco (se não existir, ele cria o arquivo automaticamente)
conexao = sqlite3.connect('base_dados_mantiqueira.db')
cursor = conexao.cursor()

# 2. Criando a tabela de Controle de Qualidade (SQL puro!)
cursor.execute('''
CREATE TABLE IF NOT EXISTS qualidade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    lote TEXT,
    peso_medio REAL,
    status TEXT
)
''')

# 3. Inserindo dados de exemplo
print("Inserindo dados no Banco SQL...")
dados = [
    ('2026-01-19', 'Lote_A', 62.5, 'Aprovado'),
    ('2026-01-19', 'Lote_B', 58.2, 'Aprovado'),
    ('2026-01-19', 'Lote_C', 45.0, 'Reprovado')
]

cursor.executemany('INSERT INTO qualidade (data, lote, peso_medio, status) VALUES (?, ?, ?, ?)', dados)

# 4. Salvando e fechando
conexao.commit()
conexao.close()

print("✅ Banco de Dados 'base_dados_mantiqueira.db' criado e populado!")