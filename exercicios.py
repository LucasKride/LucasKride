print("Qual seu sexo?")
print("Homem (H) / Mulher (M)")

H = "H"
M = "M"

sexo = str(input("Digite seu sexo: "))


if(sexo == H):
    altura = float(input("Qual sua altura?: "))
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal e {}".format(peso_ideal))
elif(sexo == M):
    altura = float(input("Qual sua altura?: "))
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal e: {}".format(peso_ideal))
else:
    print("Escolha um numero valido")
