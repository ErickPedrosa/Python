cidade = input("Digite o nome da sua cidade:")

cidade = cidade.strip()
cidade = cidade[:5]

print("Sua cidade começa com santo: {}".format(bool("SANTO"in cidade.upper())))