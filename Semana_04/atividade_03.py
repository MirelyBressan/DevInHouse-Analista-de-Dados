#Crie um script que receba uma lista de e-mails e utilize o módulo re para: 
# Identificar e-mails válidos. Separar os inválidos em outro arquivo. 


import re  # módulo para usar expressões regulares

# lista de e-mails (poderia vir de um arquivo também)
emails = [
    "joao@gmail.com",
    "maria.silva@empresa.com.br",
    "pedro123@",
    "ana@site",
    "teste@dominio.com",
    "carla@meu-email.org",
    "emailinvalido.com"
]

# expressão regular simples para validar e-mails
padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# listas para separar os e-mails válidos e inválidos
validos = []
invalidos = []

# percorre todos os e-mails e verifica se são válidos
for e in emails:
    if re.match(padrao_email, e):  # se o e-mail combinar com o padrão
        validos.append(e)
    else:
        invalidos.append(e)

# grava os e-mails válidos em um arquivo
with open('emails_validos.txt', 'w') as arquivo_valido:
    for v in validos:
        arquivo_valido.write(v + '\n')

# grava os e-mails inválidos em outro arquivo
with open('emails_invalidos.txt', 'w') as arquivo_invalido:
    for i in invalidos:
        arquivo_invalido.write(i + '\n')

print("Arquivos criados com sucesso!")
print("→ emails_validos.txt")
print("→ emails_invalidos.txt")
