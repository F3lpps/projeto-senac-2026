from livro import Livro


if __name__ == "__main__":
    livro = Livro("Ensaio sobre a cegueira", "José Saramago", 4)
    livro.vender()
    assert livro.quantCopias == 3 #verifica que a quantidade de livros é igual 3
    livro.reabastecer(3)
    assert livro.quantCopias == 6