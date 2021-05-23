import random
from time import sleep
numero_maquina = random.randint(0, 10)
print('-=-'*20)
print('Estou pensando em um número entre 0 e 10. Tente advinhar...')
print('-=-'*20)
numero_usuario = int(input('Que número você acha que eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero_maquina == numero_usuario:
    print('Parabéns, você acertou!')
else:
    print('Ganhei, pensei no número {} e não em {}'.format(numero_maquina, numero_usuario))