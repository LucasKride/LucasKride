from re import X


def jogar():

    print("**************************")
    print("Bem vindo ao jogo da forca")
    print("**************************")

    palavra_secreta = "melancia".upper()
    letras_acertadas = ['_' for letras_acertadas in palavra_secreta]

    enforcou = False
    acertou  = False
    erro = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erro = erro + 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erro))

        enforcou = erro == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        print("jogando...")

    if (acertou):
        print("******Voce ganhou!******")
    else:
        print("Voce perdeu!")
    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()