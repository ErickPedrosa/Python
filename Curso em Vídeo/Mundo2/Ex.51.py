num = int(input("Digite o primeiro valor da P.A:"))
raz = int(input("Digite a razão da P.A:"))

for c in range(0, 10):
    print(" {}".format(num), end=',')
    num += raz
