import random

def jogar():

    imprimeMensagemAbertura()
    palavraSecreta = carregaPalavraSecreta()
    letras_acertadas = inicializaLetrasAcertadas(palavraSecreta)

    enforcou = False
    acertou = False
    qtdErros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        entrada = pedeEntrada()

        if(entrada in palavraSecreta):
            marcaEntradaCorreta(entrada,letras_acertadas, palavraSecreta)
        else:
            qtdErros+=1
            desenhaForca(qtdErros)

        enforcou = qtdErros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprimeMensagemAcertou()
    else:
        imprimeMensagemNaoAcertou(palavraSecreta)

def imprimeMensagemAbertura():
    print("--------------------")
    print("Jogo da forca")
    print("--------------------")

def carregaPalavraSecreta():
    arquivo = open("palavras.txt", "r")

    listaPalavras = []
    for linha in arquivo:
        linha = linha.strip()
        listaPalavras.append(linha)

    arquivo.close()

    posicaoPalavraSecreta = random.randrange(0, len(listaPalavras))

    palavraSecreta = listaPalavras[posicaoPalavraSecreta].upper()
    return palavraSecreta

def inicializaLetrasAcertadas(palavraSecreta):
    return ["_" for letra in palavraSecreta]

def pedeEntrada():
    return input("Informe a letra: ").strip().upper()

def marcaEntradaCorreta(entrada,letras_acertadas, palavraSecreta):
    posicao = 0
    for letra in palavraSecreta:
        if entrada == letra:
            letras_acertadas[posicao] = letra
        posicao += 1

def desenhaForca(qtdErros):
    print("  _______     ")
    print(" |/      |    ")

    if(qtdErros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(qtdErros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(qtdErros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(qtdErros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(qtdErros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(qtdErros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (qtdErros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprimeMensagemAcertou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimeMensagemNaoAcertou(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == "__main__"):
    jogar()


