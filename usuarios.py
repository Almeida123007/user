print("--------------sistema de usuario--------------")
print("--------------seja bem vindo-----------------")
usuario = []

while True:

    print("--------------menu--------------")
    print("1 - cadastrar usuario")
    print("2 - listar usuarios")
    print("3 - remover usuario")
    print("0 - sair do programa")

    opçao = input("Digite a opção desejada: ")

    if opçao == "1":
        novo_usuario = input("Digite o nome do novo usuário: ")
        usuario.append(novo_usuario)
        print(f"Usuário {novo_usuario} cadastrado com sucesso!")
    elif opçao == "2":
        for i, usuarios in enumerate(usuario, start=1):
            print(f"{i}. {usuarios}")
    elif opçao == "3":
        usuario_remover = input("Digite o nome do usuário a ser removido: ")
        usuario.remove(usuario_remover)
        print(f"Usuário {usuario_remover} removido com sucesso!")
    elif opçao == "0":
        print("Saindo do programa...")
        break