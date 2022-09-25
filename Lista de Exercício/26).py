primeiro = int(input('Informe o preço: '))
segundo  = int(input('Informe o preço: '))
terceiro = int(input('Informe o preço: '))

menor = primeiro

if (segundo < menor):
        menor = segundo
if (terceiro < menor):
        menor = terceiro

print('Menor preço: ',menor)
