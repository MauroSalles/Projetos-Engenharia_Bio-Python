import pandas as pd
import matplotlib.pyplot as plt

# 1. Registro de paradas da linha (Simulando um turno na Yakult ou Valgroup)
# O operador ou o sensor registra o motivo e quanto tempo ficou parado
dados_paradas = {
    'Motivo': ['Manutenção Corretiva', 'Troca de Lote (Setup)', 'Falta de Matéria-Prima', 
               'Ajuste de Máquina', 'Troca de Turno', 'Limpeza', 'Manutenção Corretiva'],
    'Minutos_Parados': [120, 45, 30, 15, 10, 20, 40]
}

df_paradas = pd.DataFrame(dados_paradas)

# 2. Análise de Pareto (Quais motivos somam 80% dos problemas?)
# Vamos agrupar os motivos e somar o tempo
resumo_paradas = df_paradas.groupby('Motivo')['Minutos_Parados'].sum().sort_values(ascending=False)

# 3. Cálculo do Custo de Ociosidade
# Imagine que cada minuto parado custa R$ 50,00 para a fábrica
custo_por_minuto = 50.0
custo_total_parada = resumo_paradas.sum() * custo_por_minuto

print("--- RELATÓRIO DE IMPACTO FINANCEIRO - LORENA/SP ---")
print(resumo_paradas)
print(f"\n💰 Custo Total Estimado de Paradas no Turno: R$ {custo_total_parada:,.2f}")
print("-" * 50)

# 4. Gráfico de Impacto para Reunião de Gerência
plt.figure(figsize=(10, 6))
resumo_paradas.plot(kind='bar', color='firebrick')
plt.title('Vilões da Produtividade: Tempo de Parada por Motivo')
plt.ylabel('Minutos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('impacto_paradas.png')
print("✅ Gráfico 'impacto_paradas.png' gerado. Pronto para a apresentação!")
plt.show()