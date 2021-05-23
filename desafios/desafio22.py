#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()
print('Nome completo maiúsculo: {}'.format(nome.upper()))
print('Nome completo minúsculo: {}'.format(nome.lower()))
print('Seu nome completo possui ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele possui {} letras'.format(separa[0], len(separa[0])))


