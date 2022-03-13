nome = input("Digite seu nome completo: ")

nome = nome.strip()
nome = nome.split()
indice = len(nome) - 1

print("Primeiro nome: {} \nÚltimo nome: {}".format(nome[0], nome[indice]))