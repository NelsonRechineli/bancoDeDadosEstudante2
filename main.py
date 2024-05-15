# Lista de estudantes (banco de dados)
estudantes = []
# Contador de IDs
contador_id = 1

# Função para adicionar um novo estudante
def adicionar_estudante():
    global contador_id
    nome = input("Digite o nome do estudante: ")
    idade = input("Digite a idade do estudante: ")
    curso = input("Digite o curso do estudante: ")
    estudante = {
        "id": contador_id,
        "nome": nome,
        "idade": idade,
        "curso": curso
    }
    estudantes.append(estudante)
    print(f"Estudante {nome} adicionado com sucesso com ID {contador_id}!")
    contador_id += 1

# Função para remover um estudante pelo nome ou ID
def remover_estudante():
    criterio = input("Deseja remover por (1) Nome ou (2) ID? ")
    if criterio == "1":
        nome = input("Digite o nome do estudante a ser removido: ")
        for estudante in estudantes:
            if estudante["nome"] == nome:
                estudantes.remove(estudante)
                print(f"Estudante {nome} removido com sucesso!")
                return
        print(f"Estudante {nome} não encontrado.")
    elif criterio == "2":
        id_estudante = int(input("Digite o ID do estudante a ser removido: "))
        for estudante in estudantes:
            if estudante["id"] == id_estudante:
                estudantes.remove(estudante)
                print(f"Estudante com ID {id_estudante} removido com sucesso!")
                return
        print(f"Estudante com ID {id_estudante} não encontrado.")
    else:
        print("Opção inválida.")

# Função para buscar um estudante pelo nome ou ID
def buscar_estudante():
    criterio = input("Deseja buscar por (1) Nome ou (2) ID? ")
    if criterio == "1":
        nome = input("Digite o nome do estudante a ser buscado: ")
        for estudante in estudantes:
            if estudante["nome"] == nome:
                print(f"Estudante encontrado: ID: {estudante['id']}, Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}")
                return
        print(f"Estudante {nome} não encontrado.")
    elif criterio == "2":
        id_estudante = int(input("Digite o ID do estudante a ser buscado: "))
        for estudante in estudantes:
            if estudante["id"] == id_estudante:
                print(f"Estudante encontrado: ID: {estudante['id']}, Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}")
                return
        print(f"Estudante com ID {id_estudante} não encontrado.")
    else:
        print("Opção inválida.")

# Função para listar todos os estudantes
def listar_estudantes():
    if not estudantes:
        print("Nenhum estudante cadastrado.")
        return
    for estudante in estudantes:
        print(f"ID: {estudante['id']}, Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}")

# Menu interativo
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar estudante")
        print("2. Remover estudante")
        print("3. Buscar estudante")
        print("4. Listar estudantes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_estudante()
        elif opcao == "2":
            remover_estudante()
        elif opcao == "3":
            buscar_estudante()
        elif opcao == "4":
            listar_estudantes()
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, por favor escolha uma opção válida.")

# Executa o menu
menu()
