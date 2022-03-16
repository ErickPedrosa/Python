print('-' * 40)
s = "BANCO CEV "
print(f"{s:^40}")
print('-' * 40)

valor = int(input("Qual valor você deseja sacar: R$"))

n_50 = (valor // 50)
r = (valor % 50)

n_20 = (r // 20)
r = (valor % 20)

n_10 = (r // 10)
r = (valor % 10)

n_1 = (r // 1)
r = (valor % 1)

print(f"""Total de {n_50} cédulas de R$50,00 
Total de {n_20} cédulas de R$20,00
Total de {n_10} cédulas de R$10,00
Total de {n_1} cédulas de R$1,00""")

s = "FIM DO PROGRAMA"
print(f"{s:=^40}")