correto=("b","a","b","a","c","a","e","d","e","a","c","e","d","a","b","a","b","a","c","a")
aluno=[]
x=0
z=0
p=0
y=0
a=0
while x<20:
        questoes=input("digite as questoes do aluno:")
        aluno.append(questoes)
        x+=1
        p+=1
        a+=1
        if correto[y] == aluno [y]:
            z+=1
        y+=1
        if p == 20:
            if z>=12:
                print(f"classificado e acertou {z} questoes!!")
            else:
                print(f"desclassificado pois acertou apenas {z} questoes")
        if a == 20:
            continuar= input("você deseja cadastrar outro aluno:")
            if continuar == "sim":
                x=0
                z=0
                y=0
                p=0
                a=0
                del aluno[0:20]
            elif continuar == "não":
                break
