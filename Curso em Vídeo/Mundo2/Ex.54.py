from datetime import date

now = date.today().year
menores = 0
maiores = 0

for c in range(0, 7):
    num = int(input("Digite a data de nascimento da pessoa {}: ".format(c + 1)))
    idade = now - num
    if(idade < 18):
        menores += 1
    else:
        maiores += 1

print("{} das pessoas são maiores de idade\n{} das pessoas são menores de idade".format(maiores, menores))

