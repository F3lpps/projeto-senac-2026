from datetime import time

from Veiculo import Veiculo

class Vaga:

    veiculo: Veiculo
    capacidade: int
    horario_entrada: time
    disponível = True

    def __init__(self, veiculo:Veiculo, capacidade:int, horario_entrada:time):
        self.veiculo = veiculo
        self.capacidade = capacidade
        self.horario_entrada = horario_entrada
