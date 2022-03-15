from random import randint
from time import sleep

print("=I=" * 30)
print(" JOKENPÔ")
print("=I=" * 30)

res_comp = randint(1, 3)
# 1 - Pedra;
# 2 - Papel;
# 3 - Tesoura;

print("\nCarregando...")
sleep(3)

res_user = input("\nEscolha pedra, papel ou tesoura: ")
res_user = res_user.lower()
res_user = res_user.strip()

if(res_comp == 1):
    res_comp = "pedra"; 
elif(res_comp == 2):
    res_comp = "papel"; 
elif(res_comp == 3):
    res_comp = "tesoura"; 

print("Calculando quem ganhou ...")


#Vitória da máquina;
if((res_user == "pedra" and res_comp == "papel") or (res_user == "papel" and res_comp == "tesoura") or (res_user == "tesoura" and res_comp == "pedra")):
    print('\n')
    print("=I=" * 30)
    print("\nA máquina escolheu {}\n\nQue pena, você PERDEU..".format(res_comp))
    print('\n')
    print("=I=" * 30)
#Vitória do usuário;
elif((res_user == "papel" and res_comp == "pedra") or (res_user == "tesoura" and res_comp == "papel") or (res_user == "pedra" and res_comp == "tesoura")):
    print('\n')
    print("=I=" * 30)
    print("\nA máquina escolheu {}\n\nPARABÉNS, VOCÊ GANHOU..".format(res_comp))
    print('\n')
    print("=I=" * 30)
#Empate;
elif((res_user == "pedra" and res_comp == "pedra") or (res_user == "papel" and res_comp == "papel") or (res_user == "tesoura" and res_comp == "tesoura")):
    print('\n')
    print("=I=" * 30)
    print("\nA máquina escolheu {}\n\nVocês empataram..".format(res_comp))
    print('\n')
    print("=I=" * 30)
else:
    print("ERRO: Entrada inválida"); 

