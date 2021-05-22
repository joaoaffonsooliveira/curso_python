# ANOTAÇÕES DA AULA

# O python já vem com algumas funcionalidades prontas. Entretanto, outras podemos importar.
# exemplo do import doces --> importa todos os doces
# diferente do From doces import pudim --> importa o pudim da biblioteca doces
# Da biblioteca Math temos (ceil, floor, trunc, pow, sqrt, factorial)
# exemplo import Math --> importa todas as funcionalidades acima
# exemplo From Math import sqrt --> importa a funcionalidade sqrt da biblioteca Math

# CÓDIGOS DA AULA

import math
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, (raiz))) # math.floor(raiz) math.ceil(raiz)

import random
num1 = random.random()
num2 = random.randint(1, 10)
print(num1, num2)