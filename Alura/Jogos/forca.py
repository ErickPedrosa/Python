
def jogar_forca():
    print("*"*30)
    print("Bem vindo ao jogo da forca!!!")
    print("*"*30)

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra: ")
        chute = chute.strip()


        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f"Encontrei a letra {letra} na posição {index}")

            index += 1
        

    print("*"*30)
    print("Fim do jogo!!!")
    print("*"*30)

if(__name__ == "__main__"):
    jogar_forca()