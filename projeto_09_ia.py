import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Buscar dados do Banco SQL que criamos no 08.B
conexao = sqlite3.connect('base_dados_mantiqueira.db')
df = pd.read_sql_query("SELECT peso_medio, status FROM qualidade", conexao)
conexao.close()

# 2. Preparar os dados para a IA
# Transformamos 'Aprovado' em 1 e 'Reprovado' em 0 para o computador entender
df['status_num'] = df['status'].map({'Aprovado': 1, 'Reprovado': 0})

# Criamos mais dados fictícios para a IA treinar melhor (já que temos poucos no banco)
dados_extras = pd.DataFrame({
    'peso_medio': [60.5, 42.1, 59.8, 44.2, 63.0, 41.5, 58.0, 43.8] * 10,
    'status_num': [1, 0, 1, 0, 1, 0, 1, 0] * 10
})
df_final = pd.concat([df[['peso_medio', 'status_num']], dados_extras])

# 3. Treinar o Modelo
X = df_final[['peso_medio']] # O que a IA olha (Peso)
y = df_final['status_num']   # O que a IA deve prever (Status)

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2)

modelo = RandomForestClassifier()
modelo.fit(X_treino, y_treino)

# 4. Testar a IA
previsoes = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, previsoes)

print(f"🤖 IA Treinada! Precisão do modelo: {acuracia * 100:.2f}%")

# 5. Desafio Final: Prever um novo lote
novo_peso = [[48.5]] # Teste um peso limítrofe
resultado = modelo.predict(novo_peso)
status = "Aprovado" if resultado[0] == 1 else "Reprovado"

print(f"🔮 Para um peso de {novo_peso[0][0]}g, a IA prevê: {status}")