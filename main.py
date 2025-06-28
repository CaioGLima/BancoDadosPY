from livro import Livro
from biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:
    print("\n=== MENU ===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input ("Ano: "))
        editora = input ("Editora: ")

        livro = Livro(titulo, autor, ano, editora)
        biblioteca.adicionar_livros(livro)

    elif opcao == "2":
        biblioteca.listar_livros()

    elif opcao == "3":
        print("Programa Encerrado")
        break

    else:
        print("Opção Não é Válida, Porfavor selecione uma das opções existentes")