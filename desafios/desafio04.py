# Dissecando uma variável

variavel_dissecada = input('Digite a variável que você quer dissecar: ')
print('O tipo primitivo da variável {} é: '.format(variavel_dissecada), type(variavel_dissecada))
print('{} Só tem espaços?'.format(variavel_dissecada), variavel_dissecada.isspace())
print('{} É alfabético?'.format(variavel_dissecada), variavel_dissecada.isalpha())
print('{} É um número?'.format(variavel_dissecada), variavel_dissecada.isnumeric())
print('{} É alfanumérico?'.format(variavel_dissecada), variavel_dissecada.isalnum())
print('{} É maiusculo?'.format(variavel_dissecada), variavel_dissecada.isupper())
print('{} É maiusculo?'.format(variavel_dissecada), variavel_dissecada.istitle())





