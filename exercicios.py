ganho = int(input("Digite quanto voce ganha por hora: "))
horas = int(input("Digite suas horas trabalhadas: "))

salario = ganho * horas

ir   = int(salario * 0.27)
inss = int(salario * 0.08)
sind = int(salario * 0.05)
salario_liquido = salario - (inss + ir + sind)

print("--Seu salario bruto foi:       R${}".format(salario))
print("--Voce pagou para o INSS:      R${}".format(inss))
print("--Voce pagou para o sindicado: R${}".format(sind))
print("--Voce pagou para o IR:        R${}".format(ir))
print("--Seu salario liquido sera:    R${}".format(salario_liquido))

