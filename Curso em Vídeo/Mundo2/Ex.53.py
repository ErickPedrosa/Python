frase = input("Digite uma frase: ")

frase = frase.strip()
frase = frase.split()
frase =''.join(frase)
frase = frase.lower()

tam = len(frase) - 1
teste = 0

for c in range(0, len(frase)):
    if(frase[c] != frase[tam]):
        teste += 1
    tam -= 1

if(teste == 0):
    print("A frase digitada é um palíndromo.")
else:
    print("A frase digitada não é um palíndromo.")
