import pandas as pd

# 1. Configurações de Insumos (Exemplo: Resina Plástica para a Valgroup ou Frascos para a Yakult)
insumos = {
    'Item': ['Resina PEAD', 'Rótulos', 'Tampas', 'Leite em Pó'],
    'Estoque_Atual': [5000, 120000, 80000, 2000], # kg ou unidades
    'Consumo_Diario_Medio': [800, 15000, 15000, 300],
    'Tempo_Entrega_Fornecedor_Dias': [5, 3, 3, 7], # Lead Time
    'Estoque_Seguranca_Minimo': [1000, 20000, 20000, 500]
}

df_estoque = pd.DataFrame(insumos)

# 2. Lógica de Engenharia: Cálculo do Ponto de Pedido (PP)
# Fórmula: (Consumo Diário * Tempo de Entrega) + Estoque de Segurança
df_estoque['Ponto_de_Pedido'] = (df_estoque['Consumo_Diario_Medio'] * df_estoque['Tempo_Entrega_Fornecedor_Dias']) + \
                                  df_estoque['Estoque_Seguranca_Minimo']

# 3. Verificação de Status: Precisamos comprar?
df_estoque['Status_Compra'] = df_estoque.apply(
    lambda x: '🚨 COMPRA CRÍTICA' if x['Estoque_Atual'] <= x['Ponto_de_Pedido'] else '✅ ESTOQUE OK', axis=1
)

# 4. Cálculo de quantos dias o estoque atual ainda dura
df_estoque['Dias_de_Autonomia'] = df_estoque['Estoque_Atual'] / df_estoque['Consumo_Diario_Medio']

print("--- SISTEMA DE GESTÃO DE SUPRIMENTOS - VALE DO PARAÍBA ---")
print(df_estoque[['Item', 'Estoque_Atual', 'Ponto_de_Pedido', 'Status_Compra', 'Dias_de_Autonomia']])

# 5. Exportando a lista de compras urgente para o setor de Suprimentos
compras_urgentes = df_estoque[df_estoque['Status_Compra'] == '🚨 COMPRA CRÍTICA']
if not compras_urgentes.empty:
    compras_urgentes.to_csv('pedidos_urgentes.csv', index=False)
    print(f"\n⚠️ Atenção! {len(compras_urgentes)} itens precisam de reposição imediata. Arquivo 'pedidos_urgentes.csv' gerado.")