num = int(input("Digite um número entre 0 e 9999: "))

num_m = num // 1000 % 10
num_c = num // 100 % 10
num_d = num // 10 % 10
num_u = num // 1 % 10

print("""
unidades: {}
dezenas: {}
centenas: {}
milhares: {}
""".format(num_u, num_d, num_c, num_m)
)