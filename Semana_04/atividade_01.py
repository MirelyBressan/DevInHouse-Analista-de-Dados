#Crie um script em Python que leia um arquivo CSV contendo informações de vendas
# (produto, quantidade e valor) e gere um novo arquivo CSV com uma coluna adicional chamada “Total”, 
# resultado da multiplicação entre quantidade e valor.

import csv  # biblioteca para trabalhar com arquivos CSV

# abre o arquivo CSV original para leitura
with open('Semana_04/vendas.csv', 'r', newline='') as arquivo_entrada:
    leitor = csv.reader(arquivo_entrada)
    cabecalho = next(leitor)  # lê a primeira linha (cabeçalho)
    
    # adiciona o nome da nova coluna
    cabecalho.append('Total')

    # cria uma lista para guardar os dados atualizados
    linhas = []
    linhas.append(cabecalho)

    # lê cada linha do arquivo
    for linha in leitor:
        produto = linha[0]
        quantidade = int(linha[1])
        valor = float(linha[2])
        
        total = quantidade * valor  
        linha.append(total)  
        
        linhas.append(linha)

# cria um novo arquivo CSV com a coluna Total
with open('Semana_04/vendas_com_total.csv', 'w', newline='') as arquivo_saida:
    escritor = csv.writer(arquivo_saida)
    escritor.writerows(linhas)

print("Arquivo 'vendas_com_total.csv' criado com sucesso!")
