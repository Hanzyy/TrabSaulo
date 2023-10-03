from array_queue_new import ArrayQueue

class Manutencao:
    def __init__(self, nome, data):
        self.nomeRodovia = nome
        self.dataManutencao = data

class Fila:
    def enfileirar(self, fila:ArrayQueue, novaManutencao):
        fila.enqueue(novaManutencao)
        return fila

    def desenfileirar(self, fila:ArrayQueue, manutencaoConcluida):
        fila.dequeue(manutencaoConcluida)
        return fila



if __name__ == "__main__":

    asfaltar = Manutencao("BR-101", "10/10/2023")
    
