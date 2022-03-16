sexo = ''

while (sexo != 'M' and sexo != 'F'):
    sexo = input("Digite o seu sexo:\n[ M ] - Para maculino\n[ F ] - Para feminino\n ").upper()
    if(sexo != 'M' and sexo != 'F'):
        print("ERRO: Entrada inválida, digite uma opção válida")


if(sexo == 'M'):
    print("O sexo digitado foi masculino.")
else:    
    print("O sexo digitado foi feminino.")
