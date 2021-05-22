# pede largura e altura da parede, calcula área e a quantidade de litros de tinta necessário
# sabendo que cada litro de tinta pinta 2 m2.

largura = float(input('Digite a largura em metros da parede: '))
altura = float (input('Digite a altura em metros da parede: '))

area = largura * altura
quantidade_de_tinta = area / 2

print('Sua parede possui uma área de {} m2 e precisará de {} L de tinta'.format(area, quantidade_de_tinta))