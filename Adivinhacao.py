print("--------------------")
print("Jogo de adivinhação")
print("--------------------")

numeroSecreto = 42
tentativas = 3
rodada = 1

while(rodada <= tentativas):

    numeroEntrada = input("Informe o número secreto: ")

    numeroEntradaConvertido = int(numeroEntrada)

    acertou = numeroSecreto == numeroEntradaConvertido
    numeroMaiorNumeroSecreto = numeroEntradaConvertido > numeroSecreto
    numeroMenorNumeroSecreto = numeroEntradaConvertido < numeroSecreto

    #print(f"{rodada}º rodada de {tentativas} tentativas")
    #o print abaixo cóntem uma String interpolation
    print("{} º rodada de {} tentativas".format(rodada, tentativas))

    if(acertou) :
        print("Você descobriu o número secreto!")
    else :
        if numeroMaiorNumeroSecreto:
            print("Você errou! Seu valor foi maior que o número secreto")
        elif(numeroMenorNumeroSecreto) :
            print("Você errou! Seu valor foi menor que o número secreto")
    rodada = rodada +1
