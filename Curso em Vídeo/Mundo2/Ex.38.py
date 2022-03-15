num = float(input("Digite um número qualquer: "))
num2 = float(input("Digite outro número qualquer: "))

if(num > num2):
    print("{} é maior que {}.".format(num, num2))
elif(num2 > num):
    print("{} é maior que {}.".format(num2, num))
else:
    print("{} e {} são iguais.".format(num, num2))
    