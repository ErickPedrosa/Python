from math import hypot

cat_o = float(input('Digite o cateto oposto: '))
cat_a = float(input('Digite o cateto adjacente: '))

print('A hipotenusa mede {:.2f}'.format(hypot(cat_a, cat_o)))
