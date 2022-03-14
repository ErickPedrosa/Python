n = float(input("Digite um número: "));
n2 = float(input("Digite outro número: "));
n3 = float(input("Digite outro número: "));

if(n > n2):
    if(n2 >n3):
        maior = n;
        menor = n3;
    else:
        menor = n2;
        if(n > n3):
            maior = n;
        else:
            maior = n3;
else:
    if(n > n3):
        maior = n2;
        menor = n3;
    else:
        menor = n;
        if(n2 > n3):
            maior = n2;
        else:
            maior = n3;

print("O maior número digitado foi o {:.2f} e o menor foi o {:.2f}".format(maior, menor));
