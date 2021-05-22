# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

# Usando módulo hipotenusa

import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('Um triângulo retângulo de cateto oposto {} e cateto adjacente {} possui uma hipotenusa de {:.3f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))

# Usando módulo
'''
import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.sqrt(math.pow(cateto_adjacente, 2) + math.pow(cateto_oposto, 2))

print('Um triângulo retângulo de cateto oposto {} e cateto adjacente {} possui uma hipotenusa de {:.3f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))
'''

# Usando a maneira matemática
'''
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1/2)

print('Um triângulo retângulo de cateto oposto {} e cateto adjacente {} possui uma hipotenusa de {:.3f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))
'''


