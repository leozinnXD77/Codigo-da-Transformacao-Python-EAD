import time
agenda = {}
while True:
    print('\n','=' * 48,'\n')
    print("====Menu da Agenda====\n")
    time.sleep(0.5)
    print("1. Adicionar Contato")
    time.sleep(0.5)
    print("2. Remover Contato")
    time.sleep(0.5)
    print("3. Buscar Contato")
    time.sleep(0.5)
    print("4. Ver Todos os Contatos")
    time.sleep(0.5)
    print("5. Sair")
    time.sleep(0.5)
    print('\n','=' * 48,'\n')
    
    escolha = input("Escolha uma opção (1-5): ")


    if escolha == '1':
        time.sleep(2)
        nome = input("\nDigite o nome do contato: ")
        
        if nome in agenda:
            time.sleep(2)
            print(f"\n❌ Erro: O contato '{nome}' já existe.")
        else:
            time.sleep(2)
            telefone = input("\nDigite o telefone: ")
            time.sleep(2)
            email = input("\nDigite o email: ")
            time.sleep(4)
            agenda[nome] = {"telefone": telefone, "email": email}
            
            print(f"\n✅ Contato '{nome}' adicionado com sucesso!")
            time.sleep(2)
    
    elif escolha == '2':
        time.sleep(2)
        nome = input("\nDigite o nome do contato para remover: ")
        if nome in agenda:
            del agenda[nome]
            time.sleep(2)
            print(f"\n🗑️ Contato '{nome}' removido.")
            time.sleep(1)
            continue
        else:
            time.sleep(2)
            print(f"\n❌ Erro: O contato '{nome}' não foi encontrado.")
            time.sleep(1)
            continue
    
    elif escolha == '3':
        nome = input("\nDigite o nome do contato para buscar: ")
        if nome in agenda:
            contato = agenda[nome]
            print(f"\n--- Detalhes do Contato: {nome} ---\n")
            time.sleep(3)
            print(f"Telefone: {contato['telefone']}")
            time.sleep(1)
            print(f"\nEmail: {contato['email']}\n")
            time.sleep(1)
            print('=' * 48,'\n')
            continue
        else:
            time.sleep(2)
            print(f"\n❌ Erro: O contato '{nome}' não foi encontrado.")
            time.sleep(1)
            continue
            
    elif escolha == '4':
        if not agenda:
            print("📝 Sua agenda está vazia.")
        else:
            print("\n--- Todos os Contatos ---")
            for nome, detalhes in agenda.items():
                print(f"Nome: {nome}")
                print(f"  Telefone: {detalhes['telefone']}")
                print(f"  Email: {detalhes['email']}")
                print("-------------------------")
            
    elif escolha == '5':
        time.sleep(3)
        print("\n👋 Saindo da agenda. Até mais!\n")
        time.sleep(2)
        print('=' * 48,'\n')
        break 
    

    else:
        time.sleep(2)
        print("\n🚫 Opção inválida. Por favor, digite um número de 1 a 5.")
        time.sleep(1)