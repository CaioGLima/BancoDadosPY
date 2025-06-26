class Livro:
    def __init__(self, titulo, autor, ano, editora, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.disponivel = disponivel 

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        return f"{self.titulo} ({self.ano}) - {self.autor} | {self.editora} [{status}]"
    
        