num_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if(num >= 0 and num <= 20):
        break
    print("Número inválido!!! Tente novamente")

print(f"O número digitado foi {num_ext[num]}")