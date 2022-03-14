from random import randint;

num = randint(0, 5);

n = int(input("Adivinhe o número entre 0 e 5 aleatoriamente gerado pela máquina: "));

if num == n:
    print("PARABÉNS VOCÊ ACERTOU!!!")
else:
    print("Você errou o número correto era {}".format(num))
