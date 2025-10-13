#Receba uma lista com números repetidos e remova as duplicatas usando set(). 
#Exiba a lista original e a lista sem repetições.

#   Lista
numeros = [2, 5, 3, 2, 8, 5, 10, 3, 8]

#Remoção dos números repetidos
sem_repeticao = list(set(numeros))

#Exibição das listas
print("Lista original:", numeros)
print("Lista sem repetições:", sem_repeticao)
