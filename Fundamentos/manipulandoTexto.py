# fatiamento de strings (por baixo dos panos temos a ideia de array)

# ANOTAÇÕES AULA

# frase[:5]
# frase[15:]
# frase[9:21:2] vai do 9 ao 20 pulando de 2 em 2
# frase[9::3] vai até o final pulando de 3 em 3
# len(frase) tamanho da string
# frase.count('o') contar quantas vezes o 'o' aparece na string
# frase.count('o', 1, 13)
# frase.find('deo')
# frase.find('android') se a string android não existe na string retorna -1
# 'curso' in frase procura curso dentro da string frase
# frase.replace('python', android) troca a palavra python por android na string
# frase.upper() transforma tudo em maiúscula
# frase.lower() transforma tudo em minúsculo
# frase.capitalize() joga toda a string para minúsculo e a primeira letra fica maiúscula
# frase.title() faz um captalize em cada palavra da string
# frase.strip() remove todos os espaços inúteis na string
# frase.rstrip() remove espaços da direita
# frase.lstrip() remove espaços da esquerda
# frase.split() divide a string em uma lista aonde cada índice da lista é uma nova lista e cada índice um caractere
# '-'.frase.join junta a frase que sofreu split colocando um traço entre as palavras