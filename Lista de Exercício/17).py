def calculo_loja_tintas(litro):
    latas = litro / 18
    if latas % 18 != 0:
        latas += 1
    preco_das_latas = latas * 80

    galoes = litro / 3.6
    if galoes % 3.6 != 0:
        galoes += 1
    preco_dos_galoes = galoes * 25

    mistura_lata = int(litro / 18.0)
    mistura_galao = int((litro - (mistura_lata * 18)) / 3.6)
    if litro - (mistura_lata * 18) % 3.6 != 0:
        mistura_galao += 1
    galoes_total = (mistura_lata * 80) + (mistura_galao * 25)

    print(f'''
        Total de Litros necessário para pintar: {litro:.0f}L
        Apenas latas de 18 litros: {latas:.0f} Und. - Preço: R$ {preco_das_latas:.2f}
        Apenas galões de 3.6 litros: {galoes:.0f} Und. - Preço: R$ {preco_dos_galoes:.2f}
        Mistura: {mistura_lata:.0f} Latas e {mistura_galao:.0f} Galões = 
        R$ {galoes_total:.2f}''')

area_pintura = float(input('Tamanho em metros quadrados da área a ser pintada: '))
litros = area_pintura / 6  * 1.1
calculo_loja_tintas(litros)
