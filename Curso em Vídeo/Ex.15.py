dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = float(input('Digite a quantidade de km percorridos com o carro: '))

tax_dia = 60 * dias
tax_km = 0.15 * km

tax_total = tax_dia + tax_km

print('Você deverá pagar {} reais pelo aluguel do carro'.format(tax_total))
