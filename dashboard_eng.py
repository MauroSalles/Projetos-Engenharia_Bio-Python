import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

# Configuração da Página
st.set_page_config(page_title="Engenharia Bio-Python", layout="wide")

st.title("🧪 Dashboard de Monitoramento de Processos")
st.sidebar.header("Menu de Controle")

# Seleção de Qual Projeto Exibir
opcao = st.sidebar.selectbox("Escolha o Módulo", ["Calculadora de pH", "Monitor de Sensores"])

if opcao == "Calculadora de pH":
    st.header("🧮 Calculadora de Equilíbrio Químico")
    col1, col2 = st.columns(2)
    
    with col1:
        pka = st.number_input("Digite o pKa", value=4.76)
        sal = st.number_input("Conc. Sal (mol/L)", value=0.1)
        acido = st.number_input("Conc. Ácido (mol/L)", value=0.1)
        
        if st.button("Calcular"):
            ph = pka + math.log10(sal/acido)
            st.success(f"O pH calculado é: {ph:.2f}")

if opcao == "Monitor de Sensores":
    st.header("📊 Análise de Sensores em Tempo Real")
    # Simulando dados
    df = pd.DataFrame({
        'Hora': list(range(24)),
        'Temp': [25, 28, 30, 40, 55, 70, 85, 90, 80, 70, 60, 50, 45, 40, 38, 35, 32, 30, 28, 27, 26, 25, 25, 25]
    })
    st.line_chart(df.set_index('Hora'))
    st.write("Análise: O sistema detectou um pico de temperatura às 07:00h.")