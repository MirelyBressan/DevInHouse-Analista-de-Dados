#Desenvolva um programa que: Leia uma data informada pelo usuário. 
# Calcule quantos dias faltam para o final do ano. 
# Mostre o dia da semana correspondente.

from datetime import datetime, date  # importa as funções para trabalhar com datas

# pede ao usuário que digite uma data no formato correto
data_texto = input("Digite uma data (no formato DD/MM/AAAA): ")

# converte o texto em uma data de verdade
data_usuario = datetime.strptime(data_texto, "%d/%m/%Y").date()

# pega o último dia do mesmo ano
fim_do_ano = date(data_usuario.year, 12, 31)

# calcula quantos dias faltam até o fim do ano
dias_restantes = (fim_do_ano - data_usuario).days

# mostra o dia da semana correspondente
# .weekday() retorna 0 = segunda, 1 = terça, ..., 6 = domingo
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
dia_semana = dias_semana[data_usuario.weekday()]

# exibe os resultados
print(f"O dia da semana é: {dia_semana}")
print(f"Faltam {dias_restantes} dias para o final do ano.")
