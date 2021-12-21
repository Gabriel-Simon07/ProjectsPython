print("--------------------")
print("Jogo de adivinhação")
print("--------------------")

numeroSecreto = 42

numeroEntrada = input("Informe o número secreto: ")

numeroEntradaConvertido = int(numeroEntrada)
acertou = numeroSecreto == numeroEntradaConvertido
numeroMaiorNumeroSecreto = numeroEntradaConvertido > numeroSecreto

if(acertou) :
    print("Você descobriu o número secreto!")
else :
    if numeroMaiorNumeroSecreto:
        print("Você errou! Seu valor foi maior que o número secreto")
    else :
        print("Você errou! Seu valor foi menor que o número secreto")

print("Fim de Jogo!")