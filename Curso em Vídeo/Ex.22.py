nome = input("Digite seu nome completo: ")

espacos = nome.count(' ')

nome_buffer = nome.split()

print("""
Seu nome em letras maiúsculas é {} 
Seu nome em letras minúsculas é {}
Seu nome tem {} letras
Seu primeiro nome tem {} letras
""".format(nome.upper(), nome.lower(), (len(nome) - espacos), len(nome_buffer[0]))
)