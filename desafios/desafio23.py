# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('milhar: {}'.format(m))
print('centena: {}'.format(c))
print('dezena: {}'.format(d))
print('unidade: {}'.format(u))

