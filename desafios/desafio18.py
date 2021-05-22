# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.



import math
graus = float(input('Digite um ângulo e saiba o seu seno, coseno e tangente: '))
radiano = math.radians(graus)
seno = math.sin(radiano)
coseno = math.cos(radiano)
tangente = math.tan(radiano)

print('O seno do ângulo {} é: {}'.format(graus, seno))
print('O coseno do ângulo {} é: {}'.format(graus, coseno))
print('A tangente do ângulo {} é: {}'.format(graus, tangente))

# forma matemática

'''
import math
graus = float(input('Digite um ângulo e saiba o seu seno, coseno e tangente: '))
radiano = (graus * math.pi) / 180

print('O seno do ângulo {} é: {}'.format(graus, math.sin(radiano)))
print('O coseno do ângulo {} é: {}'.format(graus, math.cos(radiano)))
print('A tangente do ângulo {} é: {}'.format(graus, math.tan(radiano)))
'''


