print("--------------------")
print("Jogo de adivinhação")
print("--------------------")

numeroSecreto = 42

numeroEntrada = input("Informe o número secreto: ")

numeroEntradaConvertido = int(numeroEntrada)

if(numeroSecreto == numeroEntradaConvertido) :
    print("Você descobriu o número secreto!")
else :
    if numeroEntradaConvertido > numeroSecreto:
        print("Você errou! Seu valor foi maior que o número secreto")
    else :
        print("Você errou! Seu valor foi menor que o número secreto")

print("Fim de Jogo!")