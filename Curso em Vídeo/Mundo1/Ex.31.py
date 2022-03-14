km = float("Digite a quantidade de kilometros da viagem: ")

if km <= 200:
    preco = km * 0.50;
    print("O preço da passagem será de R${:.2f}".format(preco))
else:
    preco = km * 0.45;
    print("O preço da passagem será de R${:.2f}".format(preco))
