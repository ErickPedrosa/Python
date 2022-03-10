metros = int(input('Digite a distância em metros: '))

km = metros / 1000
cm = metros * 100
mm = metros * 1000

print('{} metros pode ser convertido em:'.format(metros))
print('{} kilômetros\n{} centímetros\n{} milímetros'.format(km, cm, mm))
