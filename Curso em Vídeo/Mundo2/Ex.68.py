from random import randint


print('=-' * 30)
print("VAMOS JOGAR PAR OU ÍMPAR")
print('=-' * 30)

while True:
    n_comp = randint(1, 10)
    n_user = int(input("Digite um número: "))
    escolha = input("Par ou Ímpar [P/I]: ").strip().upper()
    res = (n_comp + n_user) % 2

    if(res == 0):
        resultado = 'P'
        frase = "DEU PAR"
    else:
        resultado = 'I'
        rase = "DEU ÍMPAR"

    print('-' * 60)
    print(f"Você jogou {n_user} e o computador {n_comp}. Total de {n_user + n_comp} {frase}")
    print('-' * 60)

    if(escolha == resultado):
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        print('=-' * 30)
    else:
        print("Você PERDEU!")
        print('=-' * 30)
        break; 

