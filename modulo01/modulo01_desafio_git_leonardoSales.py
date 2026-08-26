
import tkinter as tk
from tkinter import messagebox, ttk
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
c1_nome = "americano"
c1_estoque = 100
c1_preco = 8.90
c1_validade = "10/12/2026"
c1_descricao = "O clássico americano, com entrada direta na testa."

c2_nome = "social"
c2_estoque = 50
c2_preco = 12.90
c2_validade = "10/10/2026"
c2_descricao = "Fino, rômantico e robusto."

c3_nome = "japa"
c3_estoque = 130
c3_preco = 15.90
c3_validade = "10/12/2026"
c3_descricao = "Japa, corte autêntico."

c4_nome = "japa"
c4_estoque = 130
c4_preco = 15.90
c4_validade = "10/12/2026"
c4_descricao = "Japa, corte autêntico."

c5_nome = "japa"
c5_estoque = 130
c5_preco = 15.90
c5_validade = "10/12/2026"
c5_descricao = "Japa, corte autêntico."



print('-' * 48 + '\n')
print("Bem-vindo ao sistema de menu de cortes!","\n") 

print("Esses são todas as opções: \n")
print("1 - Cadastrar corte\n")
print("2 - Listar cortes\n")
print("3 - realizar agendamento\n")
print("0 - Sair do sistema\n")
 
print('-' * 48 + '\n')

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
        print(f"✂corte {c1_nome} cadastrado com sucesso na lista 1!✂")
 
    if c2_nome == "":
        print("cadastrando cortes...")
        time.sleep(3)
        c2_nome = input("digite o nome do corte: ")
        c2_estoque = int(input("coloque a quantidade em estoque: "))
        c2_preco = float(input("coloque o preço do corte: "))
        c2_descricao = input("descreva o corte: ")
        print(f"✂corte {c2_nome} cadastrado com sucesso na lista 2!✂")

    if c3_nome == "":
        print("cadastrando cortes...")
        time.sleep(3)
        c3_nome = input("digite o nome do corte: ")
        c3_estoque = int(input("coloque a quantidade em estoque: "))
        c3_preco = float(input("coloque o preço do corte: "))
        c3_descricao = input("descreva o corte: ")
        print(f"✂corte {c3_nome} cadastrado com sucesso na lista 3!✂")

    if c4_nome == "":
        print("cadastrando cortes...")

        c4_nome = input("digite o nome do corte: ")
        c4_estoque = int(input("coloque a quantidade em estoque: "))
        c4_preco = float(input("coloque o preço do corte: "))
        c4_descricao = input("descreva o corte: ")
        print(f"✂corte {c4_nome} cadastrado com sucesso na lista 4!✂")

    if c5_nome == 1:
        print("cadastrando cortes...")

        c5_nome = input("digite o nome do corte: ")
        c5_estoque = int(input("coloque a quantidade em estoque: "))
        c5_preco = float(input("coloque o preço do corte: "))
        c5_descricao = input("descreva o corte: ")
        print(f"✂corte {c5_nome} cadastrado com sucesso na lista 5!✂")

else: 
    print("opção inválida, tente novamente!")
