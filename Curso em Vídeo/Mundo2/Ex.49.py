num = int(input('Digite um número: '))

print('\nA tabuada do número digitado é: ')

for c in range(1, 11):
    res = num * c
    print('{} x {}  = {}'.format(num, c, res))
