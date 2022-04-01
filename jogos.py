import forca
import aula

def escolha_jogo():

    print("***************************")
    print("****Escolha o seu jogo*****")
    print("***************************")

    print("(1) Forca (2) Adivinhacao")

    jogo = int(input("Qual o jogo?: "))

    if(jogo == 1):
        print("jogando forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhacao!")
        aula.jogar()

if(__name__ == "__main__"):
    escolha_jogo()