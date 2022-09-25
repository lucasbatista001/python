metros =float (input("Digite a quantidade de metros quadrados a serem pintados: "))
litros = metros / 3

preco = 80.0
capacidade = 18

latas = litros / capacidade
total = latas * preco

print (f"Você usara {latas:,.2f} de latas de tinta")
print (f"O preco total é de R$ {total:,.2f} ")
