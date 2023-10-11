from array_queue_new import ArrayQueue
from array_stack import ArrayStack

class Manutencao:
    def __init__(self, nome, data, manutencao):
        self.nomeRodovia = nome
        self.dataManutencao = data
        self.manutencao = manutencao

    def __str__(self):
        return f'{self.manutencao} , {self.nomeRodovia} , {self.dataManutencao}'