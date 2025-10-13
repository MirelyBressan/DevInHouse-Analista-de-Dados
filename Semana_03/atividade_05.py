#Crie duas listas de compras: uma do João e outra da Maria. Use conjuntos para exibir: 
#Itens em comum; Itens exclusivos de cada um; Todos os itens sem duplicatas.

#Listas de compras
joao = ["arroz", "feijão", "macarrão", "banana", "sabão"]
maria = ["feijão", "banana", "maçã", "pão", "arroz"]

#Converter as listas para conjuntos
set_joao = set(joao)
set_maria = set(maria)

#Itens em comum
comum = set_joao & set_maria  # ou set_joao.intersection(set_maria)

#Itens exclusivos de cada um
exclusivo_joao = set_joao - set_maria  # ou set_joao.difference(set_maria)
exclusivo_maria = set_maria - set_joao

#Todos os itens sem duplicatas
todos = set_joao | set_maria  # ou set_joao.union(set_maria)

#Exibe os resultados
print("Itens em comum:", comum)
print("Itens exclusivos do João:", exclusivo_joao)
print("Itens exclusivos da Maria:", exclusivo_maria)
print("Todos os itens sem duplicatas:", todos)
