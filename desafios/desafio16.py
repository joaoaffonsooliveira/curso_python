# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float(input('Digite um número fracionário: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
# math.trunc corta a parte não inteira do número

#importando toda a biblioteca:

'''
import math
num = float(input('Digite um número fracionário: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))
'''

# Uma forma mais simples de fazer:

'''
num = float(input('Digite um número fracionário: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
'''
