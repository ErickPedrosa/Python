import math

ang_g = int(input('Digite o ângulo do círculo: '))

ang_r = math.radians(ang_g)

print('O seno do ângulo é {:.2f}'.format(math.sin(ang_r)))
print('O cosseno do ângulo é {:.2f}'.format(math.cos(ang_r)))
print('O tangente do ângulo é {:.2f}'.format(math.tan(ang_r)))
