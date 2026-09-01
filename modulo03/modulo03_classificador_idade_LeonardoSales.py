import time
from datetime import datetime

def mostrar_menu():
    print('\n','=' * 48,'\n')
    print("====Menu de Verificação de Idade====\n")
    print("1. Informar Idade e Descobrir Ano de Nascimento")
    print("2. Sair")
    print('\n','=' * 48)
    
def obter_idade_atual():

    while True:
        try:
            idade_str = input("\nDigite sua idade atual: ")
            idade = int(idade_str)
            
            if 0 <= idade <= 120: 
                time.sleep(2)
                return idade
            else:
                time.sleep(2)
                print("\nIdade inválida. Por favor, digite uma idade entre 0 e 120 anos.")
        except ValueError:
            time.sleep(2)
            print("\nEntrada inválida. Por favor, digite um número inteiro para a idade.")

def main():

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == '1':
            idade_atual = obter_idade_atual()
            
            ano_atual = datetime.now().year
            ano_nascimento = ano_atual - idade_atual
            time.sleep(2)
            print("\nCalculando seu ano de nascimento...")
            time.sleep(1)
            print(f"\nConsiderando o ano atual ({ano_atual}) e sua idade de {idade_atual} anos:")
            time.sleep(1)
            print(f"\nSeu ano de nascimento é aproximadamente: {ano_nascimento}")

            if idade_atual >= 18:
                time.sleep(1)
                print("\nVocê é **MAIOR** de idade!")
            else:
                time.sleep(1)
                print("\nVocê é **MENOR** de idade.")

        elif escolha == '2':
            time.sleep(1)
            print("\nSaindo do programa. Até mais!\n")
            time.sleep(2)
            print('=' * 48,'\n')
            break  
        else:
            time.sleep(2)
            print("Opção inválida. Por favor, escolha 1 ou 2.")
            time.sleep(1)
            continue

if __name__ == "__main__":
    main()