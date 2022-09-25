arquivo =float (input('Informe o tamanho do arquivo para donwload (em MB): '))
print
velocidade = float(input('Informe a velocidade de sua internet (em MBPS): '))

tempo = arquivo / velocidade
minuto = tempo / 60.0

print ('O tempo aproximado para download do arquivo usando este link e de: %.2f minutos'%minuto)
