# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = int(input('Velocidade registrada em km/h: '))
if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7
    print('Você foi multado por excesso de velocidade. Sua multa custa: R${}'.format(multa))
else:
    print('Carro com velocidade permitida {}'.format(velocidade_carro))