class Aluno:
    nome:str
    notas: list[int]

    def __init__(self, nome:str, notas:list[int]):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        soma: int = 0

        for nota in self.notas:
            soma = soma + nota
        
        return soma / len(self.notas)

    def verificar_situacao(self):
        if self.calcular_media() >= 7.0:
            return "Aprovado"
        
        if 5.0 < self.calcular_media() < 7.0:
            return "Recuperação"
        
        return "Reprovado"

        