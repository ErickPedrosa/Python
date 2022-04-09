from random import randint

n = randint(0, 30)
n2 = randint(0, 30)
n3 = randint(0, 30)
n4 = randint(0, 30)
n5 = randint(0, 30)

ns = (n, n2, n3, n4, n5)

for i in range(0, 5):
    if(i == 0):
        maior = ns[i]
        menor = ns[i]
    elif(ns[i] > maior):
        maior = ns[i]
    elif(ns[i] < menor):
        menor = ns[i]

print(f"Os valores sorteados foram: {n} {n2} {n3} {n4} {n5}")
print(f"O maior valor sorteado foi: {maior}")
print(f"O menor valor sorteado foi: {menor}")

