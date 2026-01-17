import math
import matplotlib.pyplot as plt
from datetime import datetime

def gerar_relatorio(pka, sal, acido, ph):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("relatorio_laboratorio.txt", "a") as arquivo:
        arquivo.write(f"\n[{data_hora}] - RESULTADO DE TAMPÃO\n")
        arquivo.write(f"pKa: {pka} | Sal: {sal} | Ácido: {acido}\n")
        arquivo.write(f"pH FINAL CALCULADO: {ph:.2f}\n")
        arquivo.write("-" * 30 + "\n")
    print("\n📄 Relatório salvo em 'relatorio_laboratorio.txt'!")

def plotar_curva(pka, conc_sal, conc_acido):
    # Criamos uma variação de concentrações para o gráfico
    proporcoes = [0.1, 0.2, 0.5, 1, 2, 5, 10]
    phs = [pka + math.log10(p) for p in proporcoes]
    
    plt.figure(figsize=(8, 5))
    plt.plot(proporcoes, phs, marker='o', color='blue', linestyle='--')
    plt.axhline(y=pka, color='red', linestyle=':', label=f'pKa ({pka})')
    
    # Destaca o ponto atual do seu cálculo
    ph_atual = pka + math.log10(conc_sal / conc_acido)
    plt.scatter([conc_sal/conc_acido], [ph_atual], color='green', s=100, label='Seu Ponto')
    
    plt.title("Curva de Resposta do Sistema Tampão")
    plt.xlabel("Proporção [Sal]/[Ácido]")
    plt.ylabel("pH da Solução")
    plt.legend()
    plt.grid(True)
    
    print("📊 Gerando gráfico da curva...")
    plt.savefig("grafico_ph.png") # Salva como imagem para o seu GitHub
    plt.show()

# --- Execução ---
print("--- MONITOR DE LABORATÓRIO v1.0 ---")
pka = float(input("Digite o pKa: "))
sal = float(input("Conc. Sal (mol/L): "))
acido = float(input("Conc. Ácido (mol/L): "))

ph_final = pka + math.log10(sal / acido)

print(f"\n✅ pH calculado: {ph_final:.2f}")

# Gera as automações
gerar_relatorio(pka, sal, acido, ph_final)
plotar_curva(pka, sal, acido)