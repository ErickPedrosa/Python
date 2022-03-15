menor = 1000000
maior = 0

for c in range(0, 5):
    peso = float(input("Digite o peso da pessoa {:.2f}: ".format(c + 1)))
    if(peso > maior):
        maior = peso
    if(peso < menor):
        menor = peso
print("O maior peso foi {:.2f}kg\nO menor peso foi {:.2f}kg".format(maior, menor))
