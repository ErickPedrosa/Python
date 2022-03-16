total = 0
p_caros = 0
barato_nome = ''
barato_preco = -1

while True:
    print('-' * 40)
    s = "LOJA SUPER BARATÃO "
    print(f"{s:^40}")
    print('-' * 40)

    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$"))

    total += preco

    if(preco > 1000):
        p_caros += 1

    if(barato_preco == -1):
        barato_preco = preco
        barato_nome = nome
    elif(preco < barato_preco):
        barato_preco = preco
        barato_nome = nome


    while True:
        print('-' * 40)
        res = input("Quer continuar: [S/N] ").strip().upper()[0]
        if(res == 'S' or res == 'N'):
            break
    if(res == 'N'):
        break

s = "FIM DO PROGRAMA"
print(f"{s:=^40}")

print(f"""O total da compra foi R${total:.2f}
Temos {p_caros} produtos custando mais de R$1000.00
O produto mais barato foi {barato_nome} que custa R${barato_preco:.2f}
""")