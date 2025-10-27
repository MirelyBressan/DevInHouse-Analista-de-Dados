#Desenvolva um programa que contenha três funções: Uma que receba uma lista 
# de números e retorne a média. Uma que retorne o maior e o menor número. 
# Uma função principal que chame as duas anteriores e exiba os resultados formatados

# função que calcula a média dos números
def calcular_media(numeros):
    soma = sum(numeros)  # soma todos os números da lista
    media = soma / len(numeros)  # divide pelo tamanho da lista
    return media

# função que encontra o maior e o menor número
def maior_e_menor(numeros):
    maior = max(numeros)  # pega o maior número
    menor = min(numeros)  # pega o menor número
    return maior, menor

# função principal que chama as outras
def main():
    # pede os números separados por espaço
    entrada = input("Digite vários números separados por espaço: ")
    
    # converte os valores digitados para uma lista de números (float ou int)
    numeros = [float(x) for x in entrada.split()]

    # chama as funções auxiliares
    media = calcular_media(numeros)
    maior, menor = maior_e_menor(numeros)

    # exibe os resultados formatados
    print(f"\nMédia dos números: {media:.2f}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")

# chama a função principal
main()
