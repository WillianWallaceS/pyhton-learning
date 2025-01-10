#Strings e funções de texto
faturamento = 1000
custo = 700
lucro = faturamento - custo

emailCliente = "emailqualquer@gmail.com"
print(faturamento)
print(custo)

print("Faturamento da empresa foi de: {}, Custo: {}, Lucro {}".format(faturamento,custo,lucro)) #jeito menos utilizado

print(f"Faturamento da empresa foi de: {faturamento:f}, Custo: {custo}, Lucro {lucro}") #jeito mais utilizado

#maiusculo
emailCliente = emailCliente.upper()
print(emailCliente)
 
#minusculo
emailCliente = emailCliente.lower()
print(emailCliente)

# encontrar um elemento dentro de um texto
print(emailCliente.find("j")) #-1 é quando não existe o elemento

#quantidade de caracteres que possui na variavel
print(len(emailCliente))

#pegar um caractere pelo indice 
print(emailCliente[0])

print(emailCliente[-4]) #de tras para frente 


#pegar um pedaço do email
print(emailCliente[4 :10])

# Trocar o pedaço do texto
novoEmail = emailCliente.replace("gmail.com" , "hotmail.com")
print(novoEmail)

nome  = "joao lira"

print(nome.capitalize()) #primeira letra maiuscula
print(nome.title())#primeiras letras de cada palavra maiuscula

# pegar o servidor de email 
posicaoArroba = emailCliente.find("@") +1
servidor = emailCliente[posicaoArroba:]
print(servidor)

# pegar o primeiro nome
posicaoPrimeiroNome = nome.find(" ")
primeiroNome = nome[:posicaoPrimeiroNome]
print(primeiroNome)

# pegar o sobrenome
sobrenome = nome[posicaoPrimeiroNome+1:] 
print(sobrenome)

# casos especiais - formatações numéricas em texto
print(f"Faturamento da empresa foi de: {faturamento:.2f}, Custo: {custo}, Lucro {lucro:.0%}")
