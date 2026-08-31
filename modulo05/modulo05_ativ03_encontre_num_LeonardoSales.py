import time
def maior_menor(lista_de_numeros):
    if not lista_de_numeros:
        return None, None

    maior_valor = max(lista_de_numeros)
    menor_valor = min(lista_de_numeros)

    return maior_valor, menor_valor
print("\n","="*32)
print("\n====Teste com uma lista de números====")
time.sleep(2)
numeros = [12, 5, 25, 8, 17, 3, 30]

maior, menor = maior_menor(numeros)

print(f"\nA lista de números é: {numeros}")
time.sleep(3)
print(f"O maior valor na lista é: {maior}")
time.sleep(3)
print(f"O menor valor na lista é: {menor}")
time.sleep(3)

print("\n====Teste com uma lista vazia=====")
lista_vazia = []
maior_vazio, menor_vazio = maior_menor(lista_vazia)

print(f"\nA lista é: {lista_vazia}")
time.sleep(3)
print(f"Maior valor: {maior_vazio}, Menor valor: {menor_vazio}\n")
print("="*32,"\n")