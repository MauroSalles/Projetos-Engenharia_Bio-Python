import pandas as pd
import matplotlib.pyplot as plt

# 1. Configurações de Tarifa (Simulando Horário de Ponta vs Fora de Ponta)
custo_kwh_fora_ponta = 0.65
custo_kwh_ponta = 1.10 # Energia é mais cara entre 18h e 21h

# 2. Dados de Consumo das Máquinas (Linha de Produção Yakult/Valgroup)
maquinas = {
    'Equipamento': ['Injetora 01', 'Rotuladora', 'Compressor', 'Sistema de Resfriamento'],
    'Potencia_kW': [50, 15, 30, 45],
    'Horas_Ligada_Dia': [20, 22, 24, 24]
}

df_energia = pd.DataFrame(maquinas)

# 3. Cálculo de Consumo Diário e Custo Estimado
df_energia['Consumo_Diario_kWh'] = df_energia['Potencia_kW'] * df_energia['Horas_Ligada_Dia']
df_energia['Custo_Diario_Estimado_R$'] = df_energia['Consumo_Diario_kWh'] * custo_kwh_fora_ponta

# 4. Simulação de Economia: E se desligarmos a Injetora no Horário de Ponta?
consumo_total = df_energia['Consumo_Diario_kWh'].sum()
custo_total = df_energia['Custo_Diario_Estimado_R$'].sum()

print("--- ANALISADOR DE CUSTOS DE UTILIDADES - LORENA ---")
print(df_energia)
print(f"\n⚡ Consumo Total da Planta: {consumo_total} kWh/dia")
print(f"💰 Gasto Estimado em Energia: R$ {custo_total:,.2f} por dia")

# 5. Gráfico de Consumo por Equipamento
plt.figure(figsize=(8, 5))
plt.pie(df_energia['Consumo_Diario_kWh'], labels=df_energia['Equipamento'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Distribuição de Consumo Energético por Setor')
plt.savefig('custo_energia.png')
plt.show()