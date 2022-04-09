
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))

n = (n1, n2, n3, n4)

par = 0
for i in range(0, 4):
    if (n[i] % 2 == 0):
        par += 1


print(f"Você digitou os valores: {n}")
print(f"O valor 9 apareceu {n.count(9)} vezes")

if (n.count(3) == 0):
    print(f"O valor 3 não foi digitado em nenhuma posição.")
else:
    print(f"O valor 3 foi digitado na posição {n.index(3)}")

if(par == 0):
    print(f"Não foram digitados valores pares")
else:
    print(f"Os valores pares digitados foram ", end = '')
    for i in n:
        if (i % 2 == 0):
            print(f"{i} ", end='')

print()
