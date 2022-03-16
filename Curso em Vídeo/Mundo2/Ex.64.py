soma = 0
counter = -1
n = 0

while (n != 999):
    n = int(input("Digite um número inteiro, digite 999 para parar de digitar: "))
    counter += 1
    if(n != 999):
        soma += n

print("Foram digitados {} números e a soma total deles foi {}".format(counter, soma))    
