from datetime import date; 

ano = int(input("Digite o seu ano de nascimento: ")); 

now = date.today().year; 
idade = now - ano; 

if(idade < 18):
    print("Você ainda não deve se alistar."); 
elif(idade == 18):
    print("Você deve se alistar este ano."); 
elif(idade > 18):
    print("Você já deve ter se alistado senão, regularize a sua situação na junta militar."); 
