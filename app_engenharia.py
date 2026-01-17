import customtkinter as ctk
import math

# Configuração básica
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def calcular():
    try:
        pka = float(entry_pka.get())
        sal = float(entry_sal.get())
        acido = float(entry_acido.get())
        
        ph = pka + math.log10(sal / acido)
        label_resultado.configure(text=f"pH Calculado: {ph:.2f}", text_color="#2ecc71")
    except Exception:
        label_resultado.configure(text="Erro: Use pontos e números!", text_color="#e74c3c")

# Criando a janela principal
app = ctk.CTk()
app.title("Engenharia Pro - Calculadora")
app.geometry("400x450")

# Elementos da Interface
label_titulo = ctk.CTkLabel(app, text="Calculadora de Tampão", font=("Roboto", 20, "bold"))
label_titulo.pack(pady=20)

entry_pka = ctk.CTkEntry(app, placeholder_text="Digite o pKa (ex: 4.76)", width=250)
entry_pka.pack(pady=10)

entry_sal = ctk.CTkEntry(app, placeholder_text="Conc. Sal (mol/L)", width=250)
entry_sal.pack(pady=10)

entry_acido = ctk.CTkEntry(app, placeholder_text="Conc. Ácido (mol/L)", width=250)
entry_acido.pack(pady=10)

btn_calcular = ctk.CTkButton(app, text="CALCULAR pH", command=calcular, font=("Roboto", 14, "bold"))
btn_calcular.pack(pady=25)

label_resultado = ctk.CTkLabel(app, text="Aguardando dados...", font=("Roboto", 16))
label_resultado.pack(pady=10)

# Inicia o aplicativo
app.mainloop()