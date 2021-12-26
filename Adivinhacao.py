import random

print("--------------------")
print("Jogo de adivinhação")
print("--------------------")

numeroSecreto = random.randrange(1, 101)
tentativas = 3

print(numeroSecreto)
for rodada in range(1, tentativas + 1):

    print("{} º rodada de {} tentativas".format(rodada, tentativas))

    numeroEntrada = input("Informe um número secreto entre 1 e 100: ")

    numeroEntradaConvertido = int(numeroEntrada)

    if(numeroEntradaConvertido < 1 or numeroEntradaConvertido > 100) :
        print("O número secreto informado é inválido, informe novamente")
        continue

    if(numeroSecreto == numeroEntradaConvertido) :
        print("Você descobriu o número secreto!")
        break
    else :
        if numeroEntradaConvertido > numeroSecreto:
            print("Você errou! Seu valor foi maior que o número secreto")
        elif(numeroEntradaConvertido < numeroSecreto) :
            print("Você errou! Seu valor foi menor que o número secreto")
print("Fim de jogo!")

