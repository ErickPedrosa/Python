from itertools import count


resp = 'N'
counter = 0
media = 0

while(resp != 'S'):
    counter += 1
    n = int(input("Digite um número inteiro: "))
    media += n
    resp = input("Você deseja parar de digitar [S/N]: ".upper())

media /= counter

print("Foram digitados {} números e a média deles é {:.2f}".format(counter, media))
