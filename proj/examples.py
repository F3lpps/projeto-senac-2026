################# Exercícios (1ª aula) #################

def calcula_area_triangulo(base: float, altura: float):
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")

def converte_temperatura_fahrenreit(graus_celsius: float):
    temperatura = (graus_celsius * (9/5)) + 32
    print(f"A temperatura em fahrenreit é: {temperatura}")

def converte_em_dolares(reais: float):
    dolares = reais / 5.04
    print(f"O valor em dólares é: {dolares}")


def verifica_membro_do_clube(nome:str, idade:int) -> str:
    if nome != "João" and idade < 28:
        return "Você não é membro do clube"
    
    return "Bem vindo ao clube!"
