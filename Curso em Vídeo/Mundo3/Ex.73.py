from operator import indexOf


tabela = ( "Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "RB Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense")
chap = "Chapecoense"

print("=---" * 30)
print(f"Lista de times do Brasileirão: {tabela}")
print("=---" * 30)
print(f"Os 5 primeiros são: {tabela[:5]}")
print("=---" * 30)
print(f"Os 4 últimos são: {tabela[16:]}")
print("=---" * 30)
print(f"Times em ordem alfabética: {sorted(tabela)}")
print("=---" * 30)
print(f"O Chapecoense está na {tabela.index(chap) + 1} posição.")
print("=---" * 30)
