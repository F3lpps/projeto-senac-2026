class Livro:

    titulo: str
    autor: str
    quantCopias: int

    def __init__(self, titulo, autor, quantCopias):
        self.titulo = titulo
        self.autor = autor
        self.quantCopias = quantCopias


    def vender(self):
        self.quantCopias -=1

    def reabastecer(self, copias:int):
        self.quantCopias = self.quantCopias + copias