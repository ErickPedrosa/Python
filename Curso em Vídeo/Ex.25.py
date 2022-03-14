nome = input("Digite seu nome:")

nome = nome.strip()


print("Você possui Silva no nome: {}".format(bool("SILVA"in nome.upper())))