num = input("Digite um número entre 0 e 9999: ")

num = num.strip()

num_m = num[0]
num_c = num[1]
num_d = num[2]
num_u = num[3]

print("""
unidades: {}
dezenas: {}
centenas: {}
milhares: {}
""".format(num_u, num_d, num_c, num_m)
)