# ler o preço de um produto e mostra o preço com desconto

preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite quantos desse produto serão comprados: '))
desconto = float(input('Digite o percentual de desconto do produto: '))

preco_descontado = preco * (1 - desconto / 100)
valor_da_compra = quantidade * preco_descontado

print('O produto custa {} com {} porcento de desconto. O preço total da sua compra é {}'.format(preco_descontado, desconto, valor_da_compra))