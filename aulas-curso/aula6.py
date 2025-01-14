#dicionário e estrutura de dados
# #dic_produtos = {"chave" : valor}

dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook":11000}

# #pegar um elemento
# print(dic_produtos["airpod"])

# #editar um elemento 
# dic_produtos["iphone"] = dic_produtos["iphone"] * 1.3
# print(dic_produtos)

# #quantidade de itens 
# print(len(dic_produtos))

# #retirar um item do dicionário
# dic_produtos.pop("airpod")

# #adicionar um item no dicionario
# dic_produtos["apple watch" ] = 2500
# print(dic_produtos)

# verificar se existe item no dicionário
# if "iphone" in dic_produtos:
#     print("Existe produto")
# else:
#     print("Não tem")


# # verificar se um valor existe nos valores do dicionário
# # se 9000 existe no meu dic_produtos .valores

# if 9000 in dic_produtos.values():
#     print("Existe")
# else:
#     print("Não existe")
porcento = 0.10
nome_produto = input("Nome do produto: ")
preco_produto = input("Preço do produto: ")

nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto

#para aumentar 10% os preços 

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco

print(dic_produtos)