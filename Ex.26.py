frase = input("Digite uma frase: ")

frase = frase.strip()
frase = frase.upper()

print("""
A letra 'a' aparece {} vezes;
Ela aparece pela primeira vez na posição {};
E aparece pela última vez na posição {};
""".format(frase.count("A"), frase.find("A"), frase.rfind("A"))
)