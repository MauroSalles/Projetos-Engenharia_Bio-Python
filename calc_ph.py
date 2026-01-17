import math

def calcular_ph():
    print("="*40)
    print("  CALCULADORA DE TAMPÃO QUÍMICO")
    print("="*40)
    
    try:
        # Entrada de dados
        pka = float(input("Digite o pKa do ácido (ex: 4.76): "))
        conc_sal = float(input("Concentração do Sal (mol/L): "))
        conc_acido = float(input("Concentração do Ácido (mol/L): "))
        
        # A fórmula química: pH = pKa + log10([Sal]/[Ácido])
        # Usamos math.log10 para logaritmo na base 10
        ph = pka + math.log10(conc_sal / conc_acido)
        
        print("-" * 40)
        print(f"✅ O pH calculado da solução é: {ph:.2f}")
        print("-" * 40)
        
    except ValueError:
        print("❌ ERRO: Digite apenas números. Use PONTO no lugar de vírgula.")
    except ZeroDivisionError:
        print("❌ ERRO: A concentração do ácido não pode ser zero.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

# ATENÇÃO: Use dois sublinhados antes e depois de 'name' e 'main'
if __name__ == "__main__":
    calcular_ph()
