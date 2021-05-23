# ANOTAÇÕES DA AULA

'''
Rotina é algo que faço constantemente. Na programação é igual... ou seja, é um bloco de funções que posso usar
sempre que houver a necessidade. Algumas funções já vem no python e outras podem ser importadas ou criadas por
nós mesmos.

ex: criar uma função que mostra linhas
obs: O def é para definir as minhas funções. Para chamar a linha é usando o nome da função
def mostralinha():
    print('-' * 20)

chamando a função criada:

mostralinha()
print('SISTEMA DE SELEÇÃO DE ALUNOS')
mostralinhas()

Existem funções sem parâmetros e funções com parâmetro

conceito de empacotar parâmetros:
def nome_da_funcao(*num)
uso isso quando não sei quantos parâmetros vou receber 

docstring é uma forma de criar um documento que explica a função que foi criada por mim
'''
def contador(i, f, p):
    """
    :param i = inicio da contagem
    :param f = final da contagem
    :param p = meio da contagem
    Função criada por joão affonso 
    """
    c = 1
    while c <= f:
        print(f'{c} ', end = ' ')
        c += p
    print('FIM!')