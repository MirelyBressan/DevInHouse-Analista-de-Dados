#Receba duas listas: uma com nomes e outra com idades. 
#Converta para um dicionário onde cada nome é uma chave e a idade é o valor correspondente.

#Duas listas: uma com nomes e outra com idades
nomes = ["Ana", "Bruno", "Carla", "Daniel"]
idades = [18, 22, 19, 25]

#Converte para dicionário (nome → idade)
pessoas = dict(zip(nomes, idades))

#Exibe o resultado
print("Lista de nomes:", nomes)
print("Lista de idades:", idades)
print("Dicionário com nomes e idades:", pessoas)
