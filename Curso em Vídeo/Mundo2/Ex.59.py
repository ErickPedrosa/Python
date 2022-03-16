
from time import sleep


num = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
resp = -1

while (resp != 5):
    sleep(5)
    print("""

    Selecione a operação que você quer realizar
    
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa
    """)
    resp = int(input())

    if(resp == 1):
        res = num + num2
        print("A soma entre {:.2f} e {:.2f} é igual a {:.2f}".format(num, num2, res))
    elif(resp == 2):
        res = num * num2
        print("A multiplicação entre {:.2f} e {:.2f} é igual a {:.2f}".format(num, num2, res))
    elif(resp == 3):
        if(num > num2):
            print("O número {:.2f} é maior que o número {:.2f}".format(num, num2))
        elif(num < num2):
            print("O número {:.2f} é maior que o número {:.2f}".format(num2, num))
        else:
            print("Os números digitados são iguais")
    elif(resp == 4):
        num = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
    else:
        if(resp != 5):
            print("ERRO: Entrada inválida!!!")
            
print("\nFIM DO PROGRAMA")