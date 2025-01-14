#FOR - Loop  e estruturas de repetição
#estrutura básica para todos os casos que vc vai ter

lista_vendas = [1000,800,3000,4000,300,1300]

meta = 1200
percentual_bonus = 0.1


for venda in lista_vendas:
        if venda >= meta:
            bonus = percentual_bonus * venda
        else: 
            bonus = 0
        print(bonus)


for i in range(10):
       print("Se inscreve no canal")

 #para cada item dentro da sua lista
for item in lista_vendas:
       print(item)

    # tudo que vc quer que seja executado várias vezes 
