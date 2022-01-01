def jogar():
    print("--------------------")
    print("Jogo da forca")
    print("--------------------")

    palavraSecreta = "batata"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        entrada = input("Informe a letra: ").strip()

        posicao = 0
        for letra in palavraSecreta:
            if (entrada.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao += 1
        print(letras_acertadas)
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
