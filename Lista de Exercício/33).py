ficha = list()

while True:
    nome = str(input('nome:'))
    matricula = int(input('numero da matricula:'))
    nota1 = float(input('nota 1:'))
    nota2 = float(input('nota 2:'))
    media = (nota1 + nota2) / 2
    ficha.append([matricula, nome, media])
    resp = str(input('quer contimuar? [s/n]'))
    if resp in 'Nn':
        break
print('=' * 50)
print(f'{"No.":<4}{"Matricula":<15}{"Nome":<10}{"Media":>8}')
print('-'*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<15}{a[1]:<10}{a[2]:>8.1f}')

