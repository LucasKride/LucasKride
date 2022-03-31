import random

print("********************************")
print("Bem vindo ao jogo da adivinhação")
print("********************************")


numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000


print("Qual nivel de dificuldade?: ")
print("(1) Facil (2) Medio (3) Dificil")
nivel = 0

while(nivel < 1 or nivel > 3):
    nivel = int(input("Digite um nivel: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5
else:
    print("Digite um nivel valido!")

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
        print("Você acertou e fez {}".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo!")

