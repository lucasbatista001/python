lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

valor = int(input("Entre com um número inteiro"))
print("")

if valor not in lista:
    print("Elemento não existe")

else:
    p = lista.index(valor)
    print("Elemento foi emcontrado na posição", p)
