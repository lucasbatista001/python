cidades=[]
p=[]
cid2=[]
tamanho=[]
x=0
y=0
z=0
while x < 6 :
    cidade=input(f"digite o nome da cidade{x+1}:")
    cidades.append(cidade)
    x+=1
    if cidade in p:
        print("nome da cidade repetida comece de novo!!")
        del cidades
        cidades=[]
        del p
        p=[]
        x=0
    else:
        p.append(cidade)
while True:
    pergunta=input("você deseja concatenar dados ao nome das cidades:")
    if pergunta == "sim":
        cidade=input("digite a cidade que você deseja adcionar:")
        cid2.append(cidade)
    elif pergunta == "nao":
        break
    else:
        print("opção invalida")

total=[]
total= cidades [:]
total.extend(cid2)
x=0
z=0
while x < len(total):
    z= len(total[x])
    tamanho.append(z)
    x+=1
maior = tamanho [0]
x=0
y=0
z=0
while x < len(tamanho):
    if tamanho [x] > maior :
        maior = tamanho [x]
        y=x
    x+=1
print(f"o nome da maior cidade é: {cidades [y]} e tem {maior} caracteres")
