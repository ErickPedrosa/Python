import adivinhacao
import forca

print("*"*22)
print("  Escolha o seu jogo  ")
print("*"*22)

jogo = int(input("Qual o jogo:\n(1) Adivinhação\n(2) Forca\n"))

if jogo == 1:
    adivinhacao.jogar_adivinhacao()
else:
    forca.jogar_forca()
