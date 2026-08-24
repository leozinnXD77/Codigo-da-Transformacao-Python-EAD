import random
import time
import math
numero_secreto = random.randint(1, 24)

tentativas = 0
tentativas = tentativas + 1

tentativas = math.ceil()
print('\n','='*30)
print("\n====🎰tigrinho Online!🎰====\n")
time.sleep(3)
while True:
    tentativas += 1
    palpite = int(input("Digite seu palpite (1 a 24): "))


    if palpite == numero_secreto:
        print("\nParabéns! Você acertou!\n")
        break

    elif palpite > numero_secreto:
        print("Errou! O número secreto é MENOR do que o seu palpite.")

    elif palpite < numero_secreto:
            print("Errou! O número secreto é MAIOR do que o seu palpite.")