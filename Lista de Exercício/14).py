pesopeixe = int(input('Digite o peso dos peixes: '))

if pesopeixe >= 50:
    E = pesopeixe - 50
    multa = E * 4.00
    print('Você exedeu em', E, 'o limite de peso permitido de peixes\nO valor de sua multa é de R$', multa)

else:
    print('Você não execeu o limite. ')
