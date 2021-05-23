# ANOTAÇÕES AULA

'''
Até agora usamos variáveis simples. ex: lanche = hamburguer
mas e se eu quiser acrescentar mais de um lanche? se eu fizer lanche = coxinha hamburguer é apagado
daí surge a necessidade de criar variáveis compostas, ou também chamadas de tuplas.
Na verdade já falamos de variáveis compostas quando estudamos strings. Uma string nada mais é que uma variável composta
as tuplas são imutáveis!
'''

# CÓDIGOS DA AULA

lanche = ('hamburgue', 'pudim', 'sorvete', 'refrigerante')
print(lanche)
print(lanche[1:3]) # Suco e pizza. Porque quando faz fatiamento o 3 é ignorado. printa 1 e 2
for comida in lanche:
    print(f'Eu vou comer {comida}') # F formatado, estrutura muito utilizada a partir do python 3.6

for cont in range(0, len(lanche)):
    print(cont, lanche[cont])