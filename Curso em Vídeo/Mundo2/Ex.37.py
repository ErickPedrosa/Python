num = int(input("Digite um número inteiro qualquer: "))
c = int(input("Selecione a base para conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n"))


if(c == 1):
    res = format(num, 'b')
    print("O valor {} em binário é '{}'".format(num, res))
elif(c == 2):
    res = format(num, 'o')
    print("O valor {} em octal é '{}'".format(num, res))
elif(c == 3):
    res = format(num, 'x')
    print("O valor {} em hexdecimal é '{}'".format(num, res))
else:
    print("ERRO: Selecione uma base existente para a conversão!!!")