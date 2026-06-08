class Pessoa:

    #Atributos
    nome:str 
    idade:int

    #Construtor
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e minha idade é {self.idade}"