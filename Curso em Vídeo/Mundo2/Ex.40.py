nota1 = float(input("Digite a sua 1ª nota: ")); 
nota2 = float(input("Digite a sua 2ª nota: ")); 

media = (nota1 + nota2) / 2; 

if(media < 5):
    print("\033[4;37;41mVocê foi REPROVADO\033[m")
elif(media >= 5 and media < 7):
    print("\033[1;33;40mVocê está na recuperação\033[m")
elif(media >= 7):
    print("\033[7;37;40mVocê foi APROVADO\033[m")
