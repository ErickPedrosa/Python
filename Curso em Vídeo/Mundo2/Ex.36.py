casa = float(input("Digite o valor total da casa: ")); 
salario = float(input("Digite o seu salário mensal: "))
anos = int(input("Digite a quantidade de anos do empréstimo: "))

prest_men = casa / (anos * 12); 
max_prest = (salario / 100) * 30; 

max_anos = 50

if(prest_men > max_prest):
    print("O seu empréstimo foi negado, você não recebe o suficiente para quitar sua dívida")
elif(anos > max_anos):
    print("O seu empréstimo foi negado, não financiamos empréstimos com mais de 50 anos de pagamento")
else:
    print("O seu empréstimo foi validado, você deverá pagar R${:.2f} por mês.".format(prest_men))
