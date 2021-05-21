#somando dois numeros

# no caso abaixo temos um erro porque estou concatenando dois números. Números no formato string

# numero1 = input('Digite o primeiro número: ')
# numero2 = input('Digite o segundo número: ')

# soma = numero1 + numero2

# print('A soma dos números é: ', soma)
# print('A soma dos números é: {}'.format(soma))

numero1 = int (input('Digite o primeiro número: '))
numero2 = int (input('Digite o segundo número: '))

soma = numero1 + numero2

# print('A soma dos números é: ', soma) # forma menos convencional de escrever o que fizemos na linha 21
#print('A soma entre', numero1, 'e', numero2, 'é:', soma) # forma menos convencional de escrever o que fizemos na linha 22
print('A soma entre dos números é: {}'.format(soma))
print('A soma entre {} e {} é: {}'.format(numero1, numero2, soma))

# ANOTAÇÕES DA AULA

# int, float, str, bool são os quatro tipos primitivos no python
# bool --> True or False (cuidado, precisa ser capitalized)
# type(variavel) --> retorna o tipo da variável
# variavel.isnumeric() --> retorna se é número
# variavel.isalpha() --> retorna se é letra
# variavel.isalnum() --> retorna se é alfanumérico
# Existem vários tipos de is




