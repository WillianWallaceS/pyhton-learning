# IF E CONDIÇÕES 

# if condição/comparação:
#     #tudo que acontece se a condição for verdadeira
# else:
#     #caso contrario tudo que acontece se a condição for falsa
#> maior que 
#< menor que 
#>= maior ou igual 
#<= menor ou igual
#==igual
# != diferente
#PRIMEIRO CENÁRIO
venda  = int(input("Quanto que o vendedor vendeu?"))
meta1 = 1300
meta2 = 2000

# if venda >= meta1 :
#     print("Vendador ganha bônus")
# else:
#     print("Vendedor não ganha bônus")

# print("Acabou o programa ")

#SEGUNDO CENÁRIO

if venda >= 2000:
    bonus = 0.13 * venda
else:
    if venda >= 1300:
        bonus = 0.10 * venda
    else: 
        bonus = 0
print("Bonus", bonus)

#TERCEIRO CENÁRIO
if venda >= 2000:
    bonus = 0.13 * venda
elif venda >=1300:
    bonus = 0.10 * venda
else:
    bonus = 0
print("Bonus", bonus)

lista_produtos = ["airpod", "apple watch", "iphone", "macbook" ]
produto_procurado = input("Pesquise o produto desejado: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Temos o produto no estoque")
else:
    print("Não possuimos o produto no estoque")

