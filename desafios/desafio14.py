#conversor de Cº para Fº

tempc = float(input('Digite a temperatura em celsius: '))

tempf = (tempc * (9/5)) + 32

print('A temperatura {}Cº equivale a {}Fº'.format(tempc, tempf))