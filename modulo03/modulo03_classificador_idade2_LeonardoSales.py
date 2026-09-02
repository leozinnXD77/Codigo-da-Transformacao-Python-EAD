import time
print('\n', '-' * 35)
idade = int(input("\nDigite a sua idade: "))
if idade < 13:
    time.sleep(2)
    print("\nVocê é uma Criança.")
    time.sleep(2)
    print('\n', '-' * 35,'\n')
elif idade < 18:
    time.sleep(2)
    print("\nVocê é um Adolescente.")
    time.sleep(2)
    print('\n', '-' * 35,'\n')
elif idade < 60:
    time.sleep(2)
    print("\nVocê é um Adulto.")
    time.sleep(2)
    print('\n', '-' * 35,'\n')
else:
    time.sleep(2)
    print("\nVocê é um Idoso.")
    time.sleep(2)
    print('\n', '-' * 35,'\n')