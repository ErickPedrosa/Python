
while True:
    print('-' * 40)
    num = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 40)

    if(num < 0):
        break; 

    print('-' * 40)
    print('\nA tabuada do número digitado é: ')
    print('-' * 40)

    for c in range(1, 11):
        res = num * c
        print(f'{num} x {c}  = {res}')
    print('-' * 40)
    
