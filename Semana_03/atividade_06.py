#Crie um dicionário onde as chaves são nomes de alunos e os valores são listas com 3 notas. 
#Calcule a média de cada aluno e exiba os aprovados (média ≥ 7).

#Dicionário com alunos e suas 3 notas
alunos = {
    "Ana": [8, 7, 9],
    "Bruno": [5, 6, 7],
    "Carla": [9, 8, 10],
    "Daniel": [6, 5, 6]
}

print("Alunos aprovados (média ≥ 7):")

#Percorre o dicionário com nome e lista de notas
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)  # soma as notas e divide pela quantidade
    if media >= 7:  # verifica se está aprovado
        print(f"{nome} - Média: {media:.1f}")
