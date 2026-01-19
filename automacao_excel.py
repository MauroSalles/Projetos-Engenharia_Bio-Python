import pandas as pd
from datetime import datetime

# 1. Simulação de dados brutos (Imagine que isso veio de um banco de dados da granja)
dados_producao = {
    'Data': ['2026-01-15', '2026-01-15', '2026-01-16', '2026-01-16', '2026-01-17'],
    'Lote': ['Lote_A', 'Lote_B', 'Lote_A', 'Lote_B', 'Lote_A'],
    'Producao_Ovos': [5000, 4800, 5100, 4700, 5200],
    'Consumo_Racao_kg': [600, 580, 610, 570, 620]
}

df = pd.DataFrame(dados_producao)

# 2. Engenharia de Dados: Criando métricas de eficiência (Conversão Alimentar)
# Quanto menos ração para mais ovos, melhor a eficiência.
df['Eficiencia'] = df['Producao_Ovos'] / df['Consumo_Racao_kg']

# 3. Gerando um resumo estatístico por Lote
resumo = df.groupby('Lote').agg({
    'Producao_Ovos': 'sum',
    'Consumo_Racao_kg': 'sum',
    'Eficiencia': 'mean'
}).reset_index()

# 4. Exportação para Excel com múltiplas abas
nome_arquivo = f"Relatorio_Producao_{datetime.now().strftime('%Y-%m-%d')}.xlsx"

with pd.ExcelWriter(nome_arquivo) as writer:
    df.to_excel(writer, sheet_name='Dados Detalhados', index=False)
    resumo.to_excel(writer, sheet_name='Resumo para Gestoria', index=False)

print(f"✅ Sucesso! O arquivo '{nome_arquivo}' foi gerado.")
print("-" * 30)
print(resumo)