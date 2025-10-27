#Divida um código em múltiplos módulos: funcoes_calculo.py (operações matemáticas simples); 
# funcoes_data.py (operações com datas); main.py (arquivo principal que importa os módulos e executa o programa).


# Arquivo principal com o uso dos modulos

import funcoes_calculo
import funcoes_data

def main():
    print("=== Sistema Modular em Python ===\n")

    # Testando as funções de cálculo
    print("Operações matemáticas:")
    a = 10
    b = 5
    print("Soma:", funcoes_calculo.somar(a, b))
    print("Subtração:", funcoes_calculo.subtrair(a, b))
    print("Multiplicação:", funcoes_calculo.multiplicar(a, b))
    print("Divisão:", funcoes_calculo.dividir(a, b))

    # Testando as funções de data
    print("\nOperações com datas:")
    print("Data atual:", funcoes_data.data_atual())

    data1 = "01/01/2025"
    data2 = "24/10/2025"
    print(f"Diferença entre {data1} e {data2}: {funcoes_data.diferenca_dias(data1, data2)} dias")

# Executa o programa
if __name__ == "__main__":
    main()
