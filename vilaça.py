import tkinter as tk
from tkinter import messagebox
import math

def calcular_raiz_quadrada():
    try:
        # Obtendo os números do campo de entrada
        numeros = entrada.get().split(',')
        resultados = []

        for numero in numeros:
            numero = numero.strip()
            num_float = float(numero)
            if num_float < 0:
                resultados.append(f"Raiz quadrada de {numero}: Número inválido.")
            else:
                resultado = math.sqrt(num_float)
                resultados.append(f"Raiz quadrada de {numero}: {resultado:.2f}")

        # Exibir resultados em uma caixa de mensagem
        messagebox.showinfo("Resultados", "\n".join(resultados))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos separados por vírgula.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de Raiz Quadrada")

# Configurando a entrada de números
entrada_label = tk.Label(janela, text="Digite os números (separados por vírgula):")
entrada_label.pack()

entrada = tk.Entry(janela, width=50)
entrada.pack()

# Botão para calcular a raiz quadrada
botao_calcular = tk.Button(janela, text="Calcular Raiz Quadrada", command=calcular_raiz_quadrada)
botao_calcular.pack()

# Executar a interface
janela.mainloop()