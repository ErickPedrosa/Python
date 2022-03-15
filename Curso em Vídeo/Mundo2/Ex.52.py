num = int(input('Digite um número inteiro: '))

total = 0

for c in range(1, num):
    if(num % c == 0):
        total += 1
if(total == 1):
    print("O número digitado é primo.")
else:
    print("O número digitado não é primo.")
