p = float(input("Digite o  preço do produto: ")); 

res = int(input("Selecione a forma de pagamento:\n1 - Dinheiro\n2 - Cheque\n3 - Cartão\n"))

if(res == 1 or res == 2):
    total = p
    total -= (p / 100) * 10
    print("O valor total a pagar será de R${:.2f}".format(total))
elif(res == 3):
    res = 0
    res = int(input("Qual a forma de pagamento no cartão:\n1 - À vista\n2 - Parcelado em até três vezes\n3 - Parcelado três vezes ou mais\n"))

    if(res == 1):
        total = p
        total -= (p / 100) * 5
        print("O valor total a pagar será de R${:.2f}".format(total))
    elif(res == 2):
        total = p
        print("O valor total a pagar será de R${:.2f}".format(total))
    elif(res == 3):
        total = p
        total += (p / 100) * 20
        print("O valor total a pagar será de R${:.2f}".format(total))
else:
    print("ERRO: Metodo inválido selecionado.")

