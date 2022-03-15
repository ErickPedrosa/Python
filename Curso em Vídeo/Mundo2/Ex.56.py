nome = ''
media = 0
maior = 0
f_20 = 0

for c in range(0, 4):
    nome = input("Digite o nome da pessoa {}: ".format(c + 1))
    idade = int(input("Digite a idade da pessoa {}: ".format(c + 1)))
    sexo = input("Digite o sexo da pessoa {}:\n[ M ] - Para maculino\n[ F ] - Para feminino\n ".format(c + 1))
    media += idade

    sexo = sexo.upper()

    if(idade > maior and sexo == 'M'):
        maior = idade
        nome_maior = nome
        
    if(idade < 20 and sexo == 'F'):
        f_20 += 1

media /= 4

print("A média de idade do grupo é: {:.2f} anos".format(media))
print("O nome do homem mais velho é: {} com {} anos".format(nome_maior, maior))
print("O número de mulheres que tem menos de 20 anos é : {}".format(f_20))
