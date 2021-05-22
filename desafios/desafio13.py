# lê salário e acrescenta % de aumento

salario = float(input('Digite o valor do seu salário: '))
percentual = float(input('Digite o percentual de aumento do seu salário: '))

salario_com_aumento = salario * (1 + percentual / 100)

print('O seu salário é {}. Com {} porcento de aumento seu salário será {}'.format(salario, percentual, salario_com_aumento))