from re import A, X
import random



def jogar():

    imprime_mensagem_abertura()


    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = incializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou  = False
    erro = 0    

    while(not enforcou and not acertou):
        
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta,letras_acertadas)

        else:
            erro = erro + 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erro))

        enforcou = erro == 7
        desenha_forca(erro)
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        print("jogando...")

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)







def imprime_mensagem_abertura():
    print("**************************")
    print("Bem vindo ao jogo da forca")
    print("**************************")

def carrega_palavra_secreta():
    arquivo = open("e:/IDE MAIN/repo/LucasKride/palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def incializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    
    return chute

def marca_chute_correto(chute, palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Voce foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   X  X     X  X   | /   ")
    print(" |    XX       XX   |/     ")
    print(" |   X  X     X  X   |      ")
    print(" |                   |      ")
    print(" \__       X       __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



if(__name__ == "__main__"):
    jogar()
