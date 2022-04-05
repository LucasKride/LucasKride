from http.client import FAILED_DEPENDENCY

from numpy import intp


def jogar():

    print("**************************")
    print("Bem vindo ao jogo da forca")
    print("**************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou  = False
    erro = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("Qual a letra? ")
        chute = chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erro = erro + 1
            print("O numero de erros foi {}".format(erro))
        
        enforcou = erro == 6
        print(letras_acertadas)
        print("jogando...")

    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()