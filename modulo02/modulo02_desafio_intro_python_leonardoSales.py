import time
from datetime import datetime

print("\n💛💙💛💙 DESAFIO EXTRA: SAUDAÇÃO + HORA ATUAL 💛💙💛💙")
time.sleep(3)

nome = input("\nDigite o seu nome: ")

hora_atual = datetime.now().strftime("%H:%M")
time.sleep(2)
print(f"\nOi, {nome}! Agora são exatamente {hora_atual}. Seja bem-vindo!\n")