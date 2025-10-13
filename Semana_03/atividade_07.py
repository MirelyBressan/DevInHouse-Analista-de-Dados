#Criar um sistema simples de cadastro de alunos que permita: 
#Adicionar alunos com suas respectivas notas; 
#Calcular a média de cada aluno; Exibir os alunos aprovados e reprovados com base na média. 
#Requisitos Listas para armazenar as notas dos alunos; 
#Dicionários para associar cada aluno às suas notas; 
#Laços de repetição para permitir múltiplos cadastros; 
#Condicionais para verificar aprovação (média ≥ 7.


#Cria um dicionário vazio para guardar os alunos e suas notas
alunos = {}

#Pergunta quantos alunos serão cadastrados
qtd = int(input("Quantos alunos deseja cadastrar? "))

# adastro dos alunos
for i in range(qtd):
    print(f"\nAluno {i+1}:")
    nome = input("Nome do aluno: ")

    notas = []  #lista para guardar as 3 notas do aluno
    for j in range(3):
        nota = float(input(f"Digite a {j+1}ª nota (0 a 10): "))
        notas.append(nota)

    #adiciona o aluno e suas notas ao dicionário
    alunos[nome] = notas

print("\nAlunos cadastrados com sucesso!\n")

#Listas para separar aprovados e reprovados
aprovados = {}
reprovados = {}

#Calcula a média de cada aluno
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)

    #Verifica se o aluno foi aprovado ou reprovado
    if media >= 7:
        aprovados[nome] = media
    else:
        reprovados[nome] = media

#Exibe resultados
print("Aprovados:")
for nome, media in aprovados.items():
    print(f"{nome}: média {media:.2f}")

print("\nReprovados:")
for nome, media in reprovados.items():
    print(f"{nome}: média {media:.2f}")
