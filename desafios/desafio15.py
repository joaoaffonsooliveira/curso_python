# Pergunta quantidade de km percorridos por um carro alugado e a quantidade de dias que foi alugado.
# Calcula o preço do aluguel do carro sabendo que custou 60 reais por dia e 0.15 reais por km rodado

km_percorridos = float(input('Informe quantos kilômetros foram percorridos pelo carro? '))
quantidade_dias = int(input('Informe por quantos dias o carro foi alugado: '))

valor = 60 * quantidade_dias + km_percorridos * 0.15

print('O valor pago pelo aluguel do carro é {:.2f}'.format(valor))