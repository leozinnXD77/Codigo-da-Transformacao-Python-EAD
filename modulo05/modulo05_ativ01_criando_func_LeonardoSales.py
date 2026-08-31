import time
def saudacao(nome):
    print(f"Olá, {nome}! Que bom te ver por aqui.\n")

print("\n","="*32)
print("\n====Primeira Função====\n")
time.sleep(5)
saudacao("João")
time.sleep(2)
saudacao("Maria")


meu_nome = "Parceiro de Programação"
time.sleep(3)
saudacao(meu_nome)
time.sleep(1)
print("="*32,"\n")
