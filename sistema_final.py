import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

print("🚀 Iniciando Sistema Integrado de Gestão (Projeto 10)...")

# --- PASSO 1: COLETA DE NOVOS DADOS ---
# Simulando dados que acabaram de chegar da linha de produção
novos_lotes = [
    {'data': '2026-01-20', 'lote': 'LOTE_Z1', 'peso': 65.2},
    {'data': '2026-01-20', 'lote': 'LOTE_Z2', 'peso': 41.8},
]

# --- PASSO 2: INTELIGÊNCIA ARTIFICIAL (TOMADA DE DECISÃO) ---
# Criando uma IA rápida para decidir o destino dos lotes
X_treino = [[60.0], [40.0], [62.0], [38.0]] # Pesos conhecidos
y_treino = [1, 0, 1, 0] # 1=Aprovado, 0=Reprovado
ia = RandomForestClassifier().fit(X_treino, y_treino)

print("🤖 IA Processando novos lotes...")

# --- PASSO 3: ARMAZENAMENTO EM SQL E PROCESSAMENTO ---
conexao = sqlite3.connect('base_dados_mantiqueira.db')
cursor = conexao.cursor()

resultados_finais = []

for item in novos_lotes:
    # IA decide o status
    predicao = ia.predict([[item['peso']]])
    status = "APROVADO" if predicao[0] == 1 else "REPROVADO"
    
    # Salva no Banco de Dados
    cursor.execute("INSERT INTO qualidade (data, lote, peso_medio, status) VALUES (?, ?, ?, ?)",
                   (item['data'], item['lote'], item['peso'], status))
    
    item['status'] = status
    resultados_finais.append(item)

conexao.commit()
print("💾 Dados salvos no Banco SQL com sucesso.")

# --- PASSO 4: RELATÓRIO AUTOMATIZADO (EXCEL) ---
df_final = pd.DataFrame(resultados_finais)
nome_excel = f"Relatorio_Final_Integrado_{datetime.now().strftime('%H%M')}.xlsx"
df_final.to_excel(nome_excel, index=False)

print(f"📊 Relatório Executivo Gerado: {nome_excel}")
print("\n✅ PROCESSO FINALIZADO COM SUCESSO!")
print(df_final)

conexao.close()