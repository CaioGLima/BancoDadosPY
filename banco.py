import sqlite3

from livro import Livro

#Conecta ao banco
def conectar():
    return sqlite3.connect("Biblioteca.db")

#Cria a tabela se não existir
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL,
            editora TEXT NOT NULL,
            disponivel INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def inserir_livro(livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, editora, disponivel)
       VALUES (?, ?, ?, ?, ?)
    """, (livro.titulo, livro.autor, livro.ano, livro.editora, int(livro.disponivel)))
    conn.commit()
    conn.close() 

def buscar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, autor, ano, editora, disponivel FROM livros")
    linhas = cursor.fetchall()
    conn.close()

    livros = []
    for linha in linhas:
        titulo, autor, ano, editora, disponivel = linha
        livro = Livro(titulo, autor, ano, editora, bool(disponivel))
        livros.append(livro)

    return livros