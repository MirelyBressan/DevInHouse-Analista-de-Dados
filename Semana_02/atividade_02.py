#Escreva um programa que receba uma entrada do usuário e identifique se ela é um número inteiro, 
#um número decimal ou uma string. Use type() e try/except para fazer o casting e a verificação.

#Entrada de dados
valor = input("Digite algo: ")

#Verificador
try:
    numero = int(valor)
    print("Você digitou um número inteiro.")
except:
    try:
        valor = valor.replace(",", ".")  # troca vírgula por ponto
        numero = float(valor)
        print("Você digitou um número decimal.")
    except:
        print("Você digitou uma string.")

