#Crie uma tupla com 5 elementos. Tente alterar um dos elementos e explique o erro que ocorre.
#Use comentários no código para justificar.

# Criando da tupla
minha_tupla = (10, 20, 30, 40, 50)

print("Tupla original:", minha_tupla)

# Tentando alterar um dos elementos
# Isso vai gerar um erro, pois tuplas são imutáveis
# minha_tupla[2] = 99  # ❌ Erro!

# Explicação:
# TypeError: 'tuple' object does not support item assignment
# Esse erro acontece porque, diferente das listas,
# as tuplas NÃO permitem mudar, adicionar ou remover elementos após serem criadas.

print("Tupla continua igual:", minha_tupla)
