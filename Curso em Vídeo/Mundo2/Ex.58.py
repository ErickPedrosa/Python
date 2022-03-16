from random import randint;

num = randint(0, 10); 
palpite = -1; 
n_de_palpites = 0; 


print("Adivinhe o número entre 0 e 10 aleatoriamente gerado pela máquina!!!"); 

while (palpite != num):
    palpite = int(input("Qual seu palpite: ")); 
    n_de_palpites += 1;  
    if(palpite != num and palpite != -1):
        print("Que pena você errou, tente novamente...")
print("\nParabéns, você acertou, o número gerado pela máquina foi {}\nVocê precisou de {} tentativas para acertá-lo".format(num, n_de_palpites))
