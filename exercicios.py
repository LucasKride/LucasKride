import random

print("********************************")
print("Bem vindo ao jogo da adivinhação")
print("********************************")


numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print("Qual nivel de dificuldade?: ")
print("(1) Facil (2) Medio (3) Dificil")

def get_nivel():    
    nivel = int(input("Digite um nível: "))
    if (nivel == 1):
        tentativas = 20
        return True
    elif (nivel == 2):
        tentativas = 10
        return True
    elif (nivel == 3):
        tentativas = 5
        return True
    else:
        print("Digite uma opção válida.")
        return False

validateInput = False
while not validateInput:
    validateInput = get_nivel()

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}". format(rodada, total_de_tentativas))
    chute_str = input("Digite seu numero entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue


    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        print("O numero secreto é {}". format(numero_secreto))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
            print("O numero secreto eh {}". format(numero_secreto))

print("Fim do jogo!")

