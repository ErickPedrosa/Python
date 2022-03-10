largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
tinta = area / 2

print('A área da parede equivale a {:.2f} e serão necessários {:.1f} litros de tinta para pintá-la'.format(area, tinta))
