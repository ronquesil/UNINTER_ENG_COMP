import os  # Importe a biblioteca 'os' para limpar a tela do console

# Variável global para armazenar o ID dos livros
id_global = 1

# Lista de dicionários para armazenar os livros
lista_livro = []

# Função para limpar a tela do console
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para cadastrar um livro
def cadastrar_livro(id):
    global id_global
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite a editora do livro: ")

    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    lista_livro.append(livro)
    id_global += 1
    print("Livro cadastrado com sucesso!")

# Função para consultar todos os livros
def consultar_todos_livros():
    limpar_tela()  # Limpar a tela antes de exibir a lista de livros
    print("\n**************************************")
    print("Lista de todos os livros:")
    for livro in lista_livro:
        print("**************************************")
        print(f"ID: {livro['id']}")
        print(f"Nome: {livro['nome']}")
        print(f"Autor: {livro['autor']}")
        print(f"Editora: {livro['editora']}")
    input("\nPressione Enter para continuar...")

# Função para consultar um livro por ID
def consultar_livro_por_id():
    limpar_tela()  # Limpar a tela antes de exibir o resultado da consulta
    try:
        id_busca = int(input("Digite o ID do livro que deseja consultar: "))
        for livro in lista_livro:
            if livro['id'] == id_busca:
                print("\n**************************************")
                print(f"ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
                print("**************************************")
                input("\nPressione Enter para continuar...")
                return
        print("Livro não encontrado.")
        input("\nPressione Enter para continuar...")
    except ValueError:
        print("ID inválido. Por favor, insira um número válido.")
        input("\nPressione Enter para continuar...")

# Função para consultar livros por autor
def consultar_livros_por_autor():
    limpar_tela()  # Limpar a tela antes de exibir a lista de livros
    autor_busca = input("Digite o nome do autor que deseja consultar: ")
    print("\n**************************************")
    print(f"Lista de livros do autor {autor_busca}:")
    encontrou = False
    for livro in lista_livro:
        if livro['autor'] == autor_busca:
            print("**************************************")
            print(f"ID: {livro['id']}")
            print(f"Nome: {livro['nome']}")
            print(f"Editora: {livro['editora']}")
            encontrou = True
    if not encontrou:
        print("Nenhum livro encontrado para este autor.")
    input("\nPressione Enter para continuar...")

# Função para remover um livro
def remover_livro():
    limpar_tela()  # Limpar a tela antes de exibir o resultado da remoção
    try:
        id_remover = int(input("Digite o ID do livro que deseja remover: "))
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print("Livro removido com sucesso!")
                input("\nPressione Enter para continuar...")
                return
        print("Livro não encontrado.")
        input("\nPressione Enter para continuar...")
    except ValueError:
        print("ID inválido. Por favor, insira um número válido.")
        input("\nPressione Enter para continuar...")

# Função principal
def main():
    while True:
        limpar_tela()  # Limpar a tela antes de exibir o MENU PRINCIPAL
        print("Bem-vindo ao Controle de livros do Ronaldo Queiroz da Silva")
        print("**************************************")
        print("----------------------MENU PRINCIPAL----------------------------")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")
        print("**************************************")
        opcao_principal = input("Escolha uma opção: ")

        if opcao_principal == "1":
            while True:
                limpar_tela()  # Limpar a tela antes de exibir o MENU CADASTRAR LIVRO
                print("Bem-vindo ao Controle de livros do Ronaldo Queiroz da Silva")
                print("**************************************")
                print("----------------MENU CADASTRAR LIVRO-----------------")
                print("1. Cadastrar um Livro")
                print("2. Retornar ao Menu Principal")
                print("**************************************")
                opcao_cadastrar = input("Escolha uma opção: ")
                if opcao_cadastrar == "1":
                    cadastrar_livro(id_global)
                elif opcao_cadastrar == "2":
                    break
                else:
                    print("Opção inválida!")

        elif opcao_principal == "2":
            while True:
                limpar_tela()  # Limpar a tela antes de exibir o MENU CONSULTAR LIVRO
                print("Bem-vindo ao Controle de livros do Ronaldo Queiroz da Silva")
                print("**************************************")
                print("---------------MENU CONSULTAR LIVRO-----------------")
                print("1. Consultar Todos")
                print("2. Consultar por Id")
                print("3. Consultar por Autor")
                print("4. Retornar ao Menu Principal")
                print("**************************************")
                opcao_consultar = input("Escolha uma opção: ")
                if opcao_consultar == "1":
                    consultar_todos_livros()
                elif opcao_consultar == "2":
                    consultar_livro_por_id()
                elif opcao_consultar == "3":
                    consultar_livros_por_autor()
                elif opcao_consultar == "4":
                    break
                else:
                    print("Opção inválida!")

        elif opcao_principal == "3":
            remover_livro()
        elif opcao_principal == "4":
            print("Programa encerrado. Obrigado!")
            break
        else:
            print("Opção inválida!")

# Executa a função principal
if __name__ == "__main__":
    main()
