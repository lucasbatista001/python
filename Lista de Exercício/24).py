frase = input('Digite tres palavra: ').split()
tam_palavras = list()
for palavra in frase:
    tam_palavras.append(len(palavra))

maior = max(tam_palavras)
print('Maior palavra:')
for a, b in zip(frase, tam_palavras):
    if b == maior:
        print(a)
        print(len(a))

