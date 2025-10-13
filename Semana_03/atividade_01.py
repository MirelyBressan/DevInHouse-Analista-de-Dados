#Dado um dicionário com produtos e preços, 
#exiba apenas os produtos com preço acima de R$ 100. Use items() e if.

#Dicionário com produtos e preços
produtos = {
    "Camisa": 80,
    "Calça": 120,
    "Tênis": 250,
    "Boné": 60,
    "Jaqueta": 300
}

#Exibição dos produtos com preço maior que 100
print("Produtos com preço acima de R$ 100:")

for nome, preco in produtos.items():  
    if preco > 100:  
        print(f"{nome}: R$ {preco}")
