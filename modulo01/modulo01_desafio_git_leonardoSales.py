import time
'''

>>projeto barbearia:

>PO (Como dono do negócio: Quero um sistema de cortes para minha barbearia,
para que eu possa controlar quais cortes e agendamentos.)

>QA (Como cliente: Quero um sistema de cortes para minha barbearia, 
para que eu possa escolher meus cortes de forma mais fácil e rápida.)

>Tech (Como programador: Quero um sistema inteligente de cortes para minha barbearia, 
para que eu possa desenvolver um software de mais qualidade e eficiência para o negócio.)

>Dev (como programador: Quero um sistema de cortes para minha barbearia, 
para que eu possa aplicar funcionalidades interessantes para atender
 necessidades do negócio e do cliente.)

>UX (Como designer de exxperiência do usuário: quero um sistema de cortes para minha barbearia, 
para que eu possa criar uma interface limpa e flúida para os usuários, garantindo 
uma experiência satisfatória.)

>IA (Como analista de dados: Quero um sistema de cortes para minha barbearia,
 para que eu possa identificar padrões, criar algoritimos de consumo e 
 recomendações em Marketing.)


'''
c1_nome = ""
c1_estoque = 0
c1_preco = 0
c1_validade = ""
c1_descricao = ""

c2_nome = ""
c2_estoque = 0
c2_preco = 0
c2_validade = ""
c2_descricao = ""

c3_nome = ""
c3_estoque = 0
c3_preco = 0                      #<-- blocos de variáveis.
c3_validade = ""
c3_descricao = ""

c4_nome = ""
c4_estoque = 0
c4_preco = 0
c4_validade = ""
c4_descricao = ""

c5_nome = ""
c5_estoque = 0
c5_preco = 0
c5_validade = ""
c5_descricao = ""

while True:
#======================MENU=========================
    print('-' * 48 + '\n')
    print("Bem-vindo ao sistema de menu de cortes!","\n") 

    print("Esses são todas as opções: \n")
    print("1 - Cadastrar corte\n")
    print("2 - Listar cortes\n")
    print("3 - realizar agendamento\n")
    print("0 - Sair do sistema\n")
    
    print('-' * 48 + '\n')
#======================MENU============================

#------------------------------------------------------

#======================OPÇÃO 1=========================
    opcao = int(input('escolha sua opção: '))

    if opcao == 1:
        if c1_nome == "":
            print("\ncadastrando cortes...")
            time.sleep(3)
            c1_nome = input("\ndigite o nome do corte: ")
            time.sleep(2)
            c1_estoque = int(input("\ncoloque a quantidade em estoque: "))
            time.sleep(4)
            c1_preco = float(input("\ncoloque o preço do corte: "))
            time.sleep(3)
            c1_descricao = input("\ndescreva o corte: ")
            time.sleep(2)
            print(f"\n✂corte {c1_nome} cadastrado com sucesso na lista 1!✂\n")
            time.sleep(2)
            continue
    
        elif c2_nome == "":
            print("cadastrando cortes...")
            time.sleep(3)
            c2_nome = input("digite o nome do corte: ")
            time.sleep(2)
            c2_estoque = int(input("coloque a quantidade em estoque: "))
            time.sleep(4)
            c2_preco = float(input("coloque o preço do corte: "))
            time.sleep(3)
            c2_descricao = input("descreva o corte: ")
            time.sleep(2)
            print(f"\n✂corte {c2_nome} cadastrado com sucesso na lista 2!✂\n")
            time.sleep(2)
            continue
        
        elif c3_nome == "":
            print("cadastrando cortes...")
            time.sleep(3)
            c3_nome = input("digite o nome do corte: ")
            time.sleep(2)
            c3_estoque = int(input("coloque a quantidade em estoque: "))
            time.sleep(4)
            c3_preco = float(input("coloque o preço do corte: "))
            time.sleep(3)
            c3_descricao = input("descreva o corte: ")
            time.sleep(2)
            print(f"\n✂corte {c3_nome} cadastrado com sucesso na lista 3!✂\n")
            time.sleep(2)
            continue
        
        elif c4_nome == "":
            print("cadastrando cortes...")

            c4_nome = input("digite o nome do corte: ")
            time.sleep(2)
            c4_estoque = int(input("coloque a quantidade em estoque: "))
            time.sleep(4)
            c4_preco = float(input("coloque o preço do corte: "))
            time.sleep(3)
            c4_descricao = input("descreva o corte: ")
            time.sleep(2)
            print(f"\n✂corte {c4_nome} cadastrado com sucesso na lista 4!✂\n")
            time.sleep(2)
            continue
        
        elif c5_nome == "":
            print("cadastrando cortes...")

            c5_nome = input("digite o nome do corte: ")
            time.sleep(2)
            c5_estoque = int(input("coloque a quantidade em estoque: "))
            time.sleep(4)
            c5_preco = float(input("coloque o preço do corte: "))
            time.sleep(3)
            c5_descricao = input("descreva o corte: ")
            time.sleep(2)
            print(f"\n✂corte {c5_nome} cadastrado com sucesso na lista 5!✂\n")
            time.sleep(2)
            continue
        
        else:
            print("Máximo de cortes cadastrados!")
            time.sleep(2)
#======================OPÇÃO 1=========================

#------------------------------------------------------

#======================OPÇÃO 2=========================
    elif opcao == 2:
            print('Listando cortes...')    
            time.sleep(2)
            if c1_nome == "" and c2_nome == "" and c3_nome == "" and c4_nome == "" and c5_nome == "":
                print('Nenhum produto cadastrado no sistema ainda.')
                continue
            else:
                print('\n','💠'*30,'\n')
                if c1_nome != "":
                    print(f"Nome: {c1_nome}, Estoque: {c1_estoque}, Preço: {c1_preco} e Descrição: '{c1_descricao}'. ")
                    
                if c2_nome != "":
                    time.sleep(3)
                    print(f"\nNome: {c2_nome}, Estoque: {c2_estoque}, Preço: {c2_preco} e Descrição: '{c2_descricao}'. ")

                if c3_nome != "":             #<-- lista os cortes cadastrados.
                    time.sleep(3)
                    print(f"\nNome: {c3_nome}, Estoque: {c3_estoque}, Preço: {c3_preco} e Descrição: '{c3_descricao}'. ")
                    
                if c4_nome != "":
                    time.sleep(3)
                    print(f"\nNome: {c4_nome}, Estoque: {c4_estoque}, Preço: {c4_preco} e Descrição: '{c4_descricao}'. ")
                    
                if c5_nome != "":
                    time.sleep(3)
                    print(f"\nNome: {c5_nome}, Estoque: {c5_estoque}, Preço: {c5_preco} e Descrição: '{c5_descricao}'. ")
                
                print('\n','💠'*30,'\n')
                time.sleep(2)
            continue
#======================OPÇÃO 2=========================

#------------------------------------------------------

#======================OPÇÃO 3=========================
    elif opcao == 3:
        print("realizando agendamento...")
        time.sleep(3)
        print('\n',"-"*30)
        print('Temos todas essas opções de cortes disponíveis: ')
        time.sleep(2)
        if c1_nome != "":
            print(f"\n1 - {c1_nome} - R${c1_preco}")
            time.sleep(2)
        if c2_nome != "":                                             #<--  mostrar cortes para venda.
            print(f"\n2 - {c2_nome} - R${c2_preco}")
            time.sleep(2)
        if c3_nome != "":
            print(f"\n3 - {c3_nome} - R${c3_preco}")
            time.sleep(2)
        if c4_nome != "":
            print(f"\n4 - {c4_nome} - R${c4_preco}")
            time.sleep(2)
        if c5_nome != "":
            print(f"\n5 - {c5_nome} - R${c5_preco}")
            time.sleep(2)
        print('\n',"-"*30)
        time.sleep(2)
        agendamento = int(input("\nEscolha o corte desejado ou aperte 0 para sair: "))
        if agendamento == 1 and c1_nome != "":
            print(f"\nAgendamento realizado com sucesso para o corte {c1_nome}!")
            time.sleep(2)
            continue
        elif agendamento == 2 and c2_nome != "":
            print(f"\nAgendamento realizado com sucesso para o corte {c2_nome}!")
            time.sleep(2)
            continue
        elif agendamento == 3 and c3_nome != "":
            print(f"\nAgendamento realizado com sucesso para o corte {c3_nome}!")            #<-- realizar venda.
            time.sleep(2)
            continue
        elif agendamento == 4 and c4_nome != "":
            print(f"\nAgendamento realizado com sucesso para o corte {c4_nome}!")
            time.sleep(2)
            continue
        elif agendamento == 5 and c5_nome != "":
            print(f"\nAgendamento realizado com sucesso para o corte {c5_nome}!")
            time.sleep(2)
            continue
        elif agendamento == 0:
            print("\nSaindo do agendamento...")
            time.sleep(2)
            continue
        else:
            print("\nOpção inválida ou corte não cadastrado, tente novamente!")
            time.sleep(2)
            continue
#======================OPÇÃO 3=========================

#opção de saida:
    elif opcao == 0:
            print('Saindo...\n')
            time.sleep(3)
            break

#opção inválida:
    else: 
        print("opção inválida, tente novamente!\n")
        time.sleep(2)
        continue