from random import randint

def jogar_adivinhacao():   
    print("*"*35)
    print("Bem vindo ao jogo de adivinhação!!!")
    print("*"*35)

    numero_secreto = randint(1, 100)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil\n")

    nivel = int(input())

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("*"*35)
        print(f"Tentativa {rodada} de {tentativas}")
        chute = int(input("\nDigite um número entre 1 e 100: "))

        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
    


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"\nVocê acertou e fez {pontos} pontos\n")
            break
        else:
            if(maior):
                print("\nVocê errou! O seu chute foi maior que o número secreto.\n")
            elif(menor):
                print("\nVocê errou! O seu chute foi menor que o número secreto.\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    


    print("*"*35)
    print("Fim do jogo!!!")
    print("*"*35)

if(__name__ == "__main__"):
    jogar_adivinhacao()
