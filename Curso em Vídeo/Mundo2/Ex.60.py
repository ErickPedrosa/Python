num = int(input("Digite um número: "))
c = 1
fat = 1

print("{}! = ".format(num), end='')
while(c < num):
    print("{} x ".format(c), end='')
    fat *= c
    c += 1
fat *= num
print("{} = {}".format(num, fat))
