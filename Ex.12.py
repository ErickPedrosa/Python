preco_n = float(input('Digite o preço normal do produto: '))

preco_l = preco_n - ((preco_n / 100) * 5)

print('O preço desse produto com 5% de desconto será {}'.format(preco_l))
