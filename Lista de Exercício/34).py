nomes = []
alturas = []
pesos = []
Cpfs = []
sexos = []

while True:

    nome = input("digite seu nome :")

    nomes.append(nome)

    altura = float(input("digite sua altura:"))

    alturas.append(altura)

    peso = float(input("digite seu peso:"))

    pesos.append(peso)

    cpf = int(input("digite seu CPF:"))

    Cpfs.append(cpf)

    sexo = input("digite seu sexo:")

    sexos.append(sexo)

    x = int(input("digite (1) para cadastrar um novo numero e (0) para sair:"))

    if x == 0:
        break

p = int(input("digite o  cpf:"))
achou = False
x = 0
while x < len(Cpfs):
    if Cpfs[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(" o imc deste CPF é:", pesos[x] / (alturas[x] ** 2))
else:
    print(f"{p} não encontrado")
