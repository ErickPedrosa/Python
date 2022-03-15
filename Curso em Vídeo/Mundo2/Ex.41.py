idade = int(input("Digite a idade do atleta: "))

if(idade <= 9 and idade >= 0):
    print("A categoria do atleta é: MIRIM")

elif(idade <= 14 and idade >= 0):
    print("A categoria do atleta é: INFANTIL")

elif(idade <= 19 and idade >= 0):
    print("A categoria do atleta é: JUNIOR")

elif(idade <= 20 and idade >= 0):
    print("A categoria do atleta é: SÊNIOR")

elif(idade > 20 and idade >= 0):
    print("A categoria do atleta é: MASTER")

else:
    print("ERRO: Idade inválida!!!")