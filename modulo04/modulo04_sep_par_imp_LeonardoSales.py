import time
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []
print('\n','=' * 48,'\n')
print("====Verificando os números...")
for numero in numeros:
    if numero % 2 == 0:
        time.sleep(2)
        print(f"\nO número {numero} é PAR.")
        pares.append(numero)
    else:

        time.sleep(2)
        print(f"\nO número {numero} é ÍMPAR.")
        impares.append(numero)
        time.sleep(0.8)
print("\n====Resultado Final====")
time.sleep(2)
print(f"\nNúmeros Pares: {pares}")
time.sleep(1)
print(f"\nNúmeros Ímpares: {impares}")
print('\n','=' * 48,'\n')
time.sleep(1)