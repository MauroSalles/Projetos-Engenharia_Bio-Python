import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulando a leitura de dados de um sensor industrial
# Em um cenário real, você leria um arquivo .csv ou .xlsx
dados_sensor = {
    'Hora': list(range(24)),
    'Temperatura': [25, 26, 27, 29, 32, 45, 60, 75, 82, 85, 83, 78, 70, 65, 60, 58, 55, 50, 48, 45, 40, 35, 30, 28]
}

# Criando um DataFrame (a "planilha" do Pandas)
df = pd.DataFrame(dados_sensor)

# 2. Inteligência de Engenharia: Análise Automática
temp_media = df['Temperatura'].mean()
temp_maxima = df['Temperatura'].max()
hora_pico = df.loc[df['Temperatura'].idxmax(), 'Hora']

print("="*40)
print("📊 RELATÓRIO TÉCNICO DE MONITORAMENTO")
print("="*40)
print(f"🌡️ Temperatura Média: {temp_media:.1f}°C")
print(f"🔥 Pico de Temperatura: {temp_maxima}°C às {hora_pico}:00h")

# 3. Tomada de Decisão (Lógica de Segurança)
limite_seguranca = 80
if temp_maxima > limite_seguranca:
    print("\n⚠️ ALERTA CRÍTICO: Superaquecimento detectado!")
    print(f"O limite de {limite_seguranca}°C foi excedido.")
else:
    print("\n✅ Operação estável: Dentro dos limites de segurança.")
print("="*40)

# 4. Visualização de Dados
plt.figure(figsize=(10, 5))
plt.plot(df['Hora'], df['Temperatura'], marker='o', color='darkorange', label='Sensor Principal')
plt.axhline(y=limite_seguranca, color='red', linestyle='--', label='Limite de Segurança')

plt.title("Monitoramento Térmico do Reator (24h)")
plt.xlabel("Hora do Dia")
plt.ylabel("Temperatura (°C)")
plt.grid(True, alpha=0.3)
plt.legend()

print("\n📈 Gerando gráfico de monitoramento...")
plt.savefig("monitoramento_sensores.png")
plt.show()