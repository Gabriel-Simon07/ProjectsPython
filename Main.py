import Forca
import Adivinhacao

def escolheJogo():
    print("--------------------")
    print("Escolha seu jogo")
    print("--------------------")

    print("(1) - Forca | (2) - Adivinhação")

    escolhaJogo = int(input())

    if(escolhaJogo == 1):
        print("Jogo escolihdo: Forca")
        Forca.jogar()
    elif (escolhaJogo == 2):
        print("Jogo escolihdo: Adivinhação")
        Adivinhacao.jogar()

if(__name__ == "main"):
    escolheJogo()