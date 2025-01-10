#INPUT DE USUÁRIO/ COMO PEGAR INFORMAÇÕES DO USUÁRIO
#INPUTS
# email = input("Escreva seu email: ")
# nome  = input("Seu Primeiro Nome: ")
# print(nome, email)

# print(f"{nome}. Verifique seu email: {email}, que enviamos um link de confirmação")

# faturamento = float(input("Escreva seu faturamento: "))
# print(f"Seu faturamento é",faturamento)

# imposto = faturamento *0.1
# print(imposto)

#LISTAS

vendas = [100, 20, 300, 50, 67]
#soma de elementos 
total_vendas = sum(vendas)
print(total_vendas)

#tamanho da lista 
quantidade_vendas = len(vendas)
print(quantidade_vendas)

#max e min
print(max(vendas))
print(min(vendas))

#valores especificos/pegar posição
print(vendas[3])

lista_produtos =["iphone", "airpod", "ipad", "macbook"]
produto_procurado = input("Pesquise o produto: ")
produto_procurado = produto_procurado.lower()#transforma em minusculo
print( produto_procurado in lista_produtos)#procurando o produto desejado na lista de produtos 

#adicionar um item a lista
lista_produtos.append("apple watch")
print(lista_produtos)

#remover um produto da lista 
lista_produtos.remove("apple watch")
print(lista_produtos)

#editar o item da minha lista 
precos = [1500, 4000, 30, 20]
precos[0] = 2000
print(precos)

#contar quantas vezes o item aparece na lista 
print(lista_produtos.count("iphone"))

#ordenar a lista 
lista_produtos.sort()
print(lista_produtos)
lista_produtos.sort(reverse=True)#ordem decrescente
print(lista_produtos)