#Variaveis 
faturamento  = 1000 #Int
custo = 700.32 #Float -> número com casa decimal

novasVendas = 100 
faturamento = faturamento + novasVendas
imposto = faturamento * 0.1

lucro = faturamento - custo - imposto
margemDeLucro = lucro / faturamento


print("Faturamento foi de",faturamento)
print("O custo foi de",custo)
print("O imposto foi de", imposto)
print("O lucro foi de",lucro)
print("A margem de lucro foi de",round(margemDeLucro, 2))

mensagem = "Se o faturamento foi de" , faturamento,"e o custo foi de",custo,"Então o lucro obtido foi de",lucro

email = "email@gmail.com" #string

teveLucro  = True #Boolean

# Mod -> % é um operador é o resto da divisão

tempoDeContrato = 170
tempoAno =  round(170 / 12, )

print("Tempo em anos", tempoAno)

tempoMeses = tempoDeContrato % 12

print("Tempo em meses",tempoMeses)

