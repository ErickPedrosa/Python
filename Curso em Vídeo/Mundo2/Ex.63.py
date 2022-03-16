n = int(input("Digite um número inteiro: "))

a = 1
b = 1
i = 0
if n == 1:
    print('0')
elif n == 2:
    print('0 1')
else:
    print('0', end=' ')
    print(a, end=' ')
    print(b, end=' ')
    while(i < (n - 3)):
   
        total = a + b
        b=a
        a= total
        print(total, end=' ')
        i += 1
print("\n")