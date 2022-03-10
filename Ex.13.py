salario_a = float(input('Digite seu salário atual: '))
taxa = int(input('Digite a taxa de aumento do salário: '))

salario_p = salario_a + ((salario_a / 100) * taxa)

print('Seu salário será {:.2f} reais após o aumento'.format(salario_p))
