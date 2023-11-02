# Variável global para armazenar o ID dos livros
id_global = 1

# Lista de dicionários para armazenar os livros
lista_livro = []

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
    print("\n**************************************************")
    print("Lista de todos os livros:")
    for livro in lista_livro:
        print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
    print("**************************************************")

# Função para consultar um livro por ID
def consultar_livro_por_id():
    id_busca = int(input("Digite o ID do livro que deseja consultar: "))
    for livro in lista_livro:
        if livro['id'] == id_busca:
            print("\n**************************************************")
            print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
            print("**************************************************")
            return
    print("Livro não encontrado.")

# Função para consultar livros por autor
def consultar_livros_por_autor():
    autor_busca = input("Digite o nome do autor que deseja consultar: ")
    print("\n**************************************************")
    print(f"Lista de livros do autor {autor_busca}:")
    for livro in lista_livro:
        if livro['autor'] == autor_busca:
            print(f"ID: {livro['id']}, Nome: {livro['nome']}, Editora: {livro['editora']}")
    if not any(livro['autor'] == autor_busca for livro in lista_livro):
        print("Nenhum livro encontrado para este autor.")
    print("**************************************************")

# Função para remover um livro
def remover_livro():
    id_remover = int(input("Digite o ID do livro que deseja remover: "))
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso!")
            return
    print("Livro não encontrado.")

# Função principal
def main():
    print("Bem-vindo ao Controle de livros do Ronaldo Queiroz da Silva")
    while True:
        print("**************************************************")
        print("--------------MENU PRINCIPAL-----------------")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")
        print("**************************************************")
        opcao_principal = input("Escolha uma opção: ")

        if opcao_principal == "1":
            while True:
                print("**************************************************")
                print("--------------MENU CADASTRAR LIVRO-----------------")
                print("1. Cadastrar um Livro")
                print("2. Retornar ao Menu Principal")
                print("**************************************************")
                opcao_cadastrar = input("Escolha uma opção: ")
                if opcao_cadastrar == "1":
                    cadastrar_livro(id_global)
                elif opcao_cadastrar == "2":
                    break
                else:
                    print("Opção inválida!")

        elif opcao_principal == "2":
            while True:
                print("**************************************************")
                print("-------------MENU CONSULTAR LIVRO-----------------")
                print("1. Consultar Todos")
                print("2. Consultar por Id")
                print("3. Consultar por Autor")
                print("4. Retornar ao Menu Principal")
                print("**************************************************")
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
