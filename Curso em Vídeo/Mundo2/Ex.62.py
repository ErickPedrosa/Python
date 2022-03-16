num = int(input("Digite o primeiro valor da P.A:"))
raz = int(input("Digite a razão da P.A:"))
c = 0

while(c < 10):
    print(" {}".format(num), end=' ')
    num += raz
    if(c == 9):
        n = int(input("\nVocê deseja imprimir mais quantos termos: "))
        c -= n
    c += 1
print("\n")
    