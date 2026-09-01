import time
usuarios = {
    "admin": "admin123",
    "joao": "senha123",
    "maria": "abc456"
}


def validar_login(nome_usuario, senha_digitada):
    if nome_usuario in usuarios:
        if usuarios[nome_usuario] == senha_digitada:
            return True 
        else:
            return False 
    else:
        return False 


while True:
    print("\n", "=" * 48)
    print("====Sistema de Login====\n")
    nome_usuario = input("\nDigite seu nome de usuário (ou 'sair' para fechar): ")
    
    if nome_usuario.lower() == 'sair':
        time.sleep(1)
        print("\n👋 Fechando o programa. Até mais!\n")
        time.sleep(2)
        print("=" * 48, "\n")
        break
    
    senha_digitada = input("\nDigite sua senha: ")

   
    if validar_login(nome_usuario, senha_digitada):
        time.sleep(2)
        print(f"\n🎉 Login bem-sucedido! Bem-vindo(a), {nome_usuario}!")
        time.sleep(2)
        print("\n", "=" * 48)
        break 
    else:
        time.sleep(1)
        print("\n❌ Login inválido. Tente novamente.")
        continue