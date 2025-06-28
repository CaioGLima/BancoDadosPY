from livro import Livro
import banco

#Cria uma lista para armazenar os livros
class Biblioteca:
    def __init__(self):
        banco.criar_tabela()  # Garante que a tabela exista

#Adiciona um novo livro a listá
    def adicionar_livros( self, livro: Livro):
        banco.inserir_livro(livro)
        print("\n Livro adicionado com sucesso!")
        print(f"{livro}")

#Mostra os livros cadastrados
    def listar_livros(self):
        livros = banco.buscar_livros()

        if not livros:
            print("Nenhum livro cadastrado")
            return
        
        print("\n--- Lista de Livros ---")
        for idx, livro in enumerate(livros, 1):
            print(f"{idx}. {livro}")
