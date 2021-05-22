#Operadores aritmeticos em python

# ANOTAÇÕES DA AULA

# adição(+), subtração(-), multiplicação(*), divisão(/), potência (**), divisão inteira(//), resto da divisão(%)
# Ordem de precedência: 1) () , **   2) *, /, //, %     3) +, -
# posso fazer potência usando ** ou pow(x, y)
# posso fazer operações aritméticas usando strings também

#CÓDIGOS DA AULA

print('=' * 20)

nome = input('Digite seu nome: ')
print('Prazer em te conhecer {:>20}!'.format(nome))  # {:^20} {:<20}

# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite outro número: '))
# print('A soma vale {}'.format(num1 + num2))

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2
print('A soma é {}, o produto vale {} e a divisão é {:.3f}'.format(s, m, d), end = ' ')
print('Divisão inteira {}, e potência {}'.format(di, e))