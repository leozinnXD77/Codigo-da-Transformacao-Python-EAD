import time
def calcular_media(notas):
    nota_minima_para_aprovar = 7.0

    if not notas:
        return "Nenhuma nota fornecida."

    media = sum(notas) / len(notas)
    print(f"A média do aluno é: {media:.2f}")

    if media >= nota_minima_para_aprovar:
        return "🎇Aprovado🎇"
    else:
        return "❌Reprovado❌"
print("\n","="*32)
print("\n--- Cena 1: Aluno Aprovado ---")
time.sleep(4)
notas_aluno1 = [8.5, 7.0, 9.0]
resultado1 = calcular_media(notas_aluno1)
time.sleep(3)
print(f"Resultado: {resultado1}\n")
time.sleep(4)
print("--- Cenário 2: Aluno Reprovado ---")
time.sleep(4)
notas_aluno2 = [5.5, 6.0, 4.5]
resultado2 = calcular_media(notas_aluno2)
time.sleep(3)
print(f"Resultado: {resultado2}\n")
time.sleep(4)
print("--- Cenário 3: Lista de notas vazia ---")
time.sleep(3)
notas_aluno3 = []
resultado3 = calcular_media(notas_aluno3)
print(f"\nResultado: {resultado3}\n")
print("="*32,"\n")