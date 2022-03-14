sal = float(input("Digite o seu salário: ")); 

aumento = 0.0; 

if (sal > 1250):
    aumento = sal / 10; 
else:
    aumento = (sal / 10) * 1.5; 

total = sal + aumento; 

print("Você receberá R${:.2f} de aumento.\nSeu novo salário será de R${:.2f}".format(aumento, total))
