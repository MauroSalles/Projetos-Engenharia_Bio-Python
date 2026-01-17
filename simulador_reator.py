import math
import matplotlib.pyplot as plt

def simular_reator():
    print("="*40)
    print("  SIMULADOR DE CINÉTICA QUÍMICA")
    print("="*40)

    # Parâmetros da Reação
    c0 = float(input("Concentração Inicial (mol/L): "))
    k = float(input("Constante de Velocidade (k): "))
    tempo_total = int(input("Tempo total de simulação (segundos): "))

    tempos = []
    concentracoes = []

    # Simulação passo a passo (C = C0 * e^(-kt))
    for t in range(tempo_total + 1):
        c_t = c0 * math.exp(-k * t)
        tempos.append(t)
        concentracoes.append(c_t)

    # Gerando o gráfico do decaimento
    plt.figure(figsize=(10, 6))
    plt.plot(tempos, concentracoes, color='red', linewidth=2, label='Reagente A')
    plt.title(f"Decaimento da Concentração no Reator (k={k})")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Concentração (mol/L)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    print("\n📈 Gerando curva de decaimento...")
    plt.savefig("cinetica_reator.png")
    plt.show()

if __name__ == "__main__":
    simular_reator()