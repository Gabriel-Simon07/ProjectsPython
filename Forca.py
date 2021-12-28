def jogar():
    print("--------------------")
    print("Jogo da forca")
    print("--------------------")

    palavraSecreta = "batata"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        entrada = input("Informe a letra: ").strip()

        posicao = 0
        for letra in palavraSecreta:
            if (entrada.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, posicao))
            posicao += 1
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
