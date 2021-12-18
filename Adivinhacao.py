print("--------------------")
print("Jogo de adivinhação")
print("--------------------")

numeroSecreto = 42

numeroEntrada = input("Informe o número secreto: ")

numeroEntradaConvertido = int(numeroEntrada)

if(numeroSecreto == numeroEntradaConvertido) :
    print("Você descobriu o número secreto!")
else :
    print("Você errou o número secreto!")

print("Fim de Jogo!")