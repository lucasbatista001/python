positivos = 0
resposta = input("Telefonou para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Esteve no local do crime? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Mora perto da vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Devia para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Já trabalhou com a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1

if positivos == 2:
    print("Suspeita")
elif positivos>=3 and  positivos<=4:
    print("Cúmplice")
elif positivos == 5:
    print("Assassino")
else:
    print("Inocente")
