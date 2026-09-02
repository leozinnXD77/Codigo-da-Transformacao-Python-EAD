import time
lista_de_compras = []

while True:
    print('\n','=' * 48,'\n')
    print("====Menu====\n")
    time.sleep(1)
    print("1. Adicionar item")
    time.sleep(0.5)
    print("2. Remover item")
    time.sleep(0.5)
    print("3. Ver a lista")
    time.sleep(0.5)
    print("4. Sair")
    time.sleep(0.5)
    print('\n','=' * 48,'\n')
    escolha = input("Escolha uma opção (1-4): ")
    if escolha == '1':
        time.sleep(2)
        item = input("\nDigite o nome do item: ")

        lista_de_compras.append(item)
        time.sleep(2)
        print(f"\n✅ '{item}' adicionado!")
        time.sleep(1)
        continue
    elif escolha == '2':
        time.sleep(2)
        item_a_remover = input("\nDigite o nome do item para remover: ")

        if item_a_remover in lista_de_compras:

            lista_de_compras.remove(item_a_remover)
            time.sleep(2)
            print(f"\n🗑️ '{item_a_remover}' removido da lista.")
            time.sleep(1)
            continue
        else:
            time.sleep(1)
            print(f"\n❌ Erro: '{item_a_remover}' não está na lista.")
            time.sleep(1)
            continue
    elif escolha == '3':
        if lista_de_compras:
            time.sleep(2)
            print("\n🛒 Sua lista de compras:\n")
            for i, item in enumerate(lista_de_compras, start=1):
                time.sleep(1)
                print(f"{i}. {item}")
                time.sleep(1)
                continue
        else:
            time.sleep(2)
            print("\n📝 Sua lista está vazia.")
            time.leep(1)
            continue
            
    elif escolha == '4':
        time.sleep(2)
        print("\n👋 Até mais!")
        time.sleep(1)
        print('\n','=' * 48,'\n')
        break 
    else:
        time.sleep(1)
        print("\n🚫 Opção inválida. Tente novamente.")
        time.sleep(2)
        continue