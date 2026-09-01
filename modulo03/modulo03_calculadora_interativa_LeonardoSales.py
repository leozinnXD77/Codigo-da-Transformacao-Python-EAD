import time
def mostrar_menu():

    print('\n','=' * 48,'\n')
    print("====Menu de Operações====\n")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Sair")
    print('\n','=' * 48)

def obter_numeros():

    while True:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            time.sleep(2)
            num2 = float(input("\nDigite o segundo número: "))
            return num1, num2
        except ValueError:
            time.sleep(1)
            print("\nEntrada inválida. Por favor, digite números válidos.")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1, 2 ou 3): ")

        if escolha == '1':
            num1, num2 = obter_numeros()
            resultado = num1 + num2
            time.sleep(2)
            print(f"\nResultado da adição: {num1} + {num2} = {resultado}")
            time.sleep(3)
        elif escolha == '2':
            num1, num2 = obter_numeros()
            resultado = num1 - num2
            time.sleep(2)
            print(f"\nResultado da subtração: {num1} - {num2} = {resultado}")
            time.sleep(3)
        elif escolha == '3':
            print("\nSaindo do programa. Até mais!\n")
            time.sleep(2)
            print('=' * 48,'\n')
            break  
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()