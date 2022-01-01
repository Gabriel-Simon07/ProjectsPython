import random

def jogar():
    print("--------------------")
    print("Jogo da forca")
    print("--------------------")

    arquivo = open("palavras.txt", "r")

    listaPalavras = []
    for linha in arquivo:
        linha =  linha.strip()
        listaPalavras.append(linha)

    arquivo.close()

    posicaoPalavraSecreta = random.randrange(0,len(listaPalavras))

    palavraSecreta = listaPalavras[posicaoPalavraSecreta].upper()
    letras_acertadas = ["_" for letra in palavraSecreta]

    enforcou = False
    acertou = False
    qtdErros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        entrada = input("Informe a letra: ").strip().upper()

        if(entrada in palavraSecreta):
            posicao = 0
            for letra in palavraSecreta:
                if entrada == letra:
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            qtdErros+=1

        enforcou = qtdErros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você acertou a palavra secreta!")
    else:
        print("Você não conseguiu acertar a palavra secreta!")
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
