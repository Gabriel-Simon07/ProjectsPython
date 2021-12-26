import random

print("--------------------")
print("Jogo de adivinhação")
print("--------------------")

numeroSecreto = random.randrange(1, 101)
tentativas = 0
pontos = 1000
print(numeroSecreto)
print("Qual o nível de dificuldade você deseja :")
print("(1) - Fácil | (2) - Médio | (3) - Díficil")

nivelDificuldade = int(input("Informe o nível "))

if(nivelDificuldade == 1):
    tentativas = 20
elif(nivelDificuldade == 2):
    tentativas = 10
else:
    tentativas = 5

for rodada in range(1, tentativas + 1):

    print("{} º rodada de {} tentativas".format(rodada, tentativas))

    numeroEntrada = int(input("Informe um número secreto entre 1 e 100: "))

    if(numeroEntrada < 1 or numeroEntrada > 100) :
        print("O número secreto informado é inválido, informe novamente")
        continue

    if(numeroSecreto == numeroEntrada) :
        print("Você descobriu o número secreto e fez {} pontos!".format(pontos))
        break
    else :
        if numeroEntrada > numeroSecreto:
            print("Você errou! Seu valor foi maior que o número secreto")
        elif(numeroEntrada < numeroSecreto) :
            print("Você errou! Seu valor foi menor que o número secreto")
        pontos_perdidos = abs(numeroSecreto - numeroEntrada)
        pontos = pontos - pontos_perdidos
print("Fim de jogo!")
