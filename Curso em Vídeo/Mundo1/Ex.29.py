vel = int(input("Digite a velocidade do carro em Km/h: "));

if vel > 80:
    multa = vel - 80;
    multa *= 7;
    print("Você ultrapassou o limite de velocidade.\nReceberá uma multa de R${},00".format(multa));
else:
    print("Você não ultrapassou o limite de velocidade.")
