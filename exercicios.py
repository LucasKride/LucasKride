
print("*******************")
print("Calculadora Simples")
print("*******************")

numero1 = 0
numero2 = 0
resultado = 0
operacao = ''

while True:

    numero1 = int(input("Digite um numero: "))
    operacao = input("Digite uma operacao: ")
    numero2 = int(input("Digite um numero: "))

    if(operacao == "+"):
        resultado = numero1 + numero2

    elif(operacao == "-"):
        resultado = numero1 - numero2

    elif(operacao == "/"):
        resultado = numero1 / numero2

    elif(operacao == '*'):
        resultado = numero1 * numero2

    else:
        print("operacao invalida!")

    print("{} {} {} = {}".format(numero1,operacao,numero2,resultado))


