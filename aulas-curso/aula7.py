#Funções e Exercícios 

"""
Bloco de texto 
Funções servem para organizar o código e caso precise repetir ele mais de uma vez 
As variaves que ce cria na função elas só existem na função

"""

lista_precos = [500, 8000, 400, 3300]

#imposto
"""
Aliquota 1 - IR
Aliquota 2 - ISS
Aliquota 3 - CSLL
"""
aliquota1  = 0.2
aliquota2 = 0.15
aliquota3  = 0.05
 #sempre começar fazendo um dps inclui os outros 
#para cada item da lista faça essas ações 
"""for preco in lista_precos:
    if preco <= 2000:
        imposto_ir = aliquota1 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = aliquota2 * preco
    imposto_clss = aliquota3 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_clss
    print(imposto_total)
"""
#FUNÇÃO
#def = define/definir
def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = aliquota1 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = aliquota2 * preco
    imposto_clss = aliquota3 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_clss
    return imposto_total

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(imposto_total)