print("--------------------")
print("Jogo de adivinhação")
print("--------------------")

numeroSecreto = 42
tentativas = 3
rodada = 1

for rodada in range(1, tentativas + 1) :

    # print(f"{rodada}º rodada de {tentativas} tentativas")
    # o print abaixo cóntem uma String interpolation
    print("{} º rodada de {} tentativas".format(rodada, tentativas))

    numeroEntrada = input("Informe um número secreto entre 1 e 100: ")

    numeroEntradaConvertido = int(numeroEntrada)

    if(numeroEntradaConvertido < 1 or numeroEntradaConvertido > 100) :
        print("O número secreto informado é inválido, informe novamente")
        continue

        acertou = numeroSecreto == numeroEntradaConvertido
        numeroMaiorNumeroSecreto = numeroEntradaConvertido > numeroSecreto
        numeroMenorNumeroSecreto = numeroEntradaConvertido < numeroSecreto

        if(acertou) :
            print("Você descobriu o número secreto!")
            break
        else :
            if numeroMaiorNumeroSecreto:
                print("Você errou! Seu valor foi maior que o número secreto")
            elif(numeroMenorNumeroSecreto) :
                print("Você errou! Seu valor foi menor que o número secreto")
    print("Fim de jogo!")

