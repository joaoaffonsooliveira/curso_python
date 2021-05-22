# ler em metros e exibe em centímetros e milímetros

numero_em_metros = float(input('Digite um número em metros que você quer saber convertido em centímetros e milímetros: '))

numero_em_centimetros = numero_em_metros * 100
numero_em_milímetros = numero_em_metros * 1000

print('O número {} m equivale a {} cm'.format(numero_em_metros, numero_em_centimetros))
print('O número {} m equivale a {} mm'.format(numero_em_metros, numero_em_milímetros))