soma = 0
counter = 0
n = 0

while (n != 999):
    n = int(input("Digite um número inteiro, digite 999 para parar de digitar: "))
    if(n == 999):
        break; 
    counter += 1
    soma += n

print(f"Foram digitados {counter} números e a soma total deles foi {soma}")    
