
p_18 = 0
h = 0
m_20 = 0

while True:
    print('-' * 40)
    s = "CADASTRE UMA PESSOA"
    print(f"{s:^40}")
    print('-' * 40)

    idade = int(input("Idade: "))
    while True:
        sexo = input("Sexo: [M/F]").strip().upper()[0]
        if(sexo == 'M' or sexo == 'F'):
            break
    
    if(idade > 18):
        p_18 += 1

    if(sexo == 'M'):
        h += 1

    if(sexo == 'F' and idade < 20):
        m_20 += 1

    while True:
        print('-' * 40)
        res = input("Quer continuar: [S/N]").strip().upper()[0]
        if(res == 'S' or res == 'N'):
            break
    if(res == 'N'):
        break

s = "FIM DO PROGRAMA"
print(f"{s:=^40}")

print(f"""Total de pessoas com mais de 18 anos: {p_18}
Ao todo temos {h} homens cadastrados.
E temos {m_20} mulheres com menos de 20 anos""")