import time
def mostrar_menu():
    
    print('\n','=' * 48,'\n')
    print("====Menu de Comparação de Números====\n")
    print("1. Comparar Dois Números")
    print("2. Sair")
    print('\n','=' * 48)

def obter_numeros():
    
    while True:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            time.sleep(2)
            num2 = float(input(f"\nDigite o segundo número: "))
            time.sleep(2)
            return num1, num2
        except ValueError:
            time.sleep(1)
            print("\nEntrada inválida. Por favor, digite números válidos.")

def verificar_par_impar(numero):

    if int(numero) % 2 == 0:
        time.sleep(3)
        return "par"
    else:
        time.sleep(3)
        return "ímpar"

def main():

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == '1':
            num1, num2 = obter_numeros()
            print(f"\nComparando {num1} e {num2}:")
            time.sleep(2)
            
            if num1 > num2:
                time.sleep(2)
                print(f"\nO maior número é: {num1}")
            elif num2 > num1:
                time.sleep(2)
                print(f"\nO maior número é: {num2}")
            else:
                time.sleep(1)
                print("\nOs números são iguais.")

            
            print(f"\n{num1} é {verificar_par_impar(num1)}.")
            time.sleep(2)
            print(f"\n{num2} é {verificar_par_impar(num2)}.")
            print('\n','=' * 48,'\n')
        elif escolha == '2':
            time.sleep(1)
            print("\nSaindo do programa. Até mais!\n")
            time.sleep(2)
            print('=' * 48,'\n')
            break 
        else:
            time.sleep(2)
            print("Opção inválida. Por favor, escolha 1 ou 2.")
            continue

if __name__ == "__main__":
    main()