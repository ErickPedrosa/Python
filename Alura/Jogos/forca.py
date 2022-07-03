from random import randrange

def jogar_forca():
    
    imprime_msg_abertura()
    
    palavra_secreta = gera_palavra_secreta()
    
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = pede_chute()


        if (chute in palavra_secreta):
            verifica_acerto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)        
        
        enforcou = (erros == 7)
        acertou = '_' not in letras_acertadas
        
        print(letras_acertadas)
        
    if(acertou):
        imprime_msg_ganhador()
    else:
        imprime_msg_perdedor(palavra_secreta)

    print("*"*30)
    print("Fim do jogo!!!")
    print("*"*30)



def imprime_msg_abertura():
    print("*"*30)
    print("Bem vindo ao jogo da forca!!!")
    print("*"*30)



def gera_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
   
    arquivo.close()
    num = randrange(0, len(palavras))
              
    palavra_secreta = palavras[num].upper()
    
    return palavra_secreta



def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]



def pede_chute():
    chute = input("Qual letra: ")
    chute = chute.strip().upper()
    return chute



def verifica_acerto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1



def imprime_msg_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
   
   
    
def imprime_msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
  

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
if(__name__ == "__main__"):
    jogar_forca()