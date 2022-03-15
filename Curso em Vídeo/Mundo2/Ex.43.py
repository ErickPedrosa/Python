print("CÁLCULO DE IMC\n"); 
h = float(input("Digite a sua altura: ")); 
p = float(input("Digite o seu peso: ")); 

imc = p / (h ** 2); 

print("\nO seu IMC é {}".format(imc)); 

if(imc < 18.5):
    print("Você está abaixo do peso."); 
elif(imc <= 25):
    print("Você está no peso ideal."); 
elif(imc <= 30):
    print("Você está com sobrepeso."); 
elif(imc <= 40):
    print("Você está com obesidade"); 
elif(imc > 40):
    print("Você está com obesidade mórbida"); 
