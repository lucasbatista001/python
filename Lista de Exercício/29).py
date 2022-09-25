salario = float(input("Por favor, informe seu salário: "))

if salario <= 280:
    aumento_1 = (salario * 20 / 100)
    salario_n1 = salario + (salario * 20 / 100)
    print("Seu salário antes do reajuste: {:.2f}".format(salario))
    print("Aumento percentual de: 20%")
    print("Valor do aumento: {:.2f}".format(aumento_1))
    print("Seu novo salário: {:.2f}".format(salario_n1))

if salario > 280 and salario <= 700:
    aumento_2 = (salario * 15 / 100)
    salario_n2 = salario + (salario * 15 / 100)
    print("Seu salário antes do reajuste: {:.2f}".format(salario))
    print("Aumento percentual de: 15%")
    print("Valor do aumento: {:.2f}".format(aumento_2))
    print("Seu novo salário: {:.2f}".format(salario_n2))

if salario > 700 and salario <= 1500:
    aumento_3 = (salario * 10 / 100)
    salario_n3 = salario + (salario * 10 / 100)
    print("Seu salário antes do reajuste: {:.2f}".format(salario))
    print("Aumento percentual de: 10%")
    print("Valor do aumento: {:.2f}".format(aumento_3))
    print("Seu novo salário: {:.2f}".format(salario_n3))

if salario > 1500:
    aumento_4 = (salario * 5 / 100)
    salario_n4 = salario + (salario * 5 / 100)
    print("Seu salário antes do reajuste: {:.2f}".format(salario))
    print("Aumento percentual de: 5%")
    print("Valor do aumento: {:.2f}".format(aumento_4))

