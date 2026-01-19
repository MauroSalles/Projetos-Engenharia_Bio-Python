import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 1. SIMULAÇÃO DE DADOS DE ALTA CADÊNCIA (Produção de 2 milhões/dia)
# Vamos monitorar a produção por minuto (Ritmo esperado: ~1400 frascos/min)
minutos_dia = 1440
ritmo_ideal = 1400 

# Criando dados normais com pequena variação (ruído)
producao_minuto = np.random.normal(ritmo_ideal, 20, minutos_dia)

# Simulando ANOMALIAS (Quedas bruscas de ritmo que indicam falha mecânica ou entupimento)
producao_minuto[500:520] = producao_minuto[500:520] * 0.4  # Queda de 60%
producao_minuto[1000:1010] = producao_minuto[1000:1010] * 0.1 # Parada quase total

df = pd.DataFrame({'producao': producao_minuto})

# 2. IA: ISOLATION FOREST (Detecta desvios e comportamentos anômalos)
ia_monitor = IsolationForest(contamination=0.03) # Esperamos 3% de anomalias
df['anomalia'] = ia_monitor.fit_predict(df[['producao']])

# -1 significa anomalia, 1 significa normal
df['status'] = df['anomalia'].map({1: 'Normal', -1: 'ALERTA: DESVIO'})

# 3. CÁLCULO DE IMPACTO (O desvio em relação a 2 milhões/dia)
total_produzido = df['producao'].sum()
perda_estimada = (ritmo_ideal * minutos_dia) - total_produzido

print(f"--- RELATÓRIO DE INTELIGÊNCIA - PLANTA LORENA ---")
print(f"Produção Total Estimada: {total_produzido:,.0f} frascos")
print(f"Déficit por Instabilidade: {perda_estimada:,.0f} frascos")
print(f"Minutos em Estado de Alerta: {len(df[df['anomalia'] == -1])} min")
print(f"-----------------------------------------------")

# 4. VISUALIZAÇÃO DO "RITMO CARDÍACO" DA FÁBRICA
plt.figure(figsize=(12, 6))
plt.plot(df['producao'], color='blue', label='Ritmo de Produção', alpha=0.5)
anomalias = df[df['anomalia'] == -1]
plt.scatter(anomalias.index, anomalias['producao'], color='red', label='Anomalia Detectada')
plt.axhline(ritmo_ideal, color='green', linestyle='--', label='Meta Ideal')
plt.title('Monitoramento Preditivo Yakult - Detecção de Desvios na Linha')
plt.xlabel('Minutos do Dia')
plt.ylabel('Frascos por Minuto')
plt.legend()
plt.savefig('monitor_ia_yakult.png')
plt.show()