from listaDuplamenteEncadeadaComIteradorFinal_Solucao import DoublyLinkedListIterator
from array_queue_new import ArrayQueue

class Objeto:
    def __init__(self, rodovia, listaCidade: DoublyLinkedListIterator):
        self.rodovia = rodovia
        self.listaCidade = listaCidade

    def __str__(self):
        return f'{self.rodovia}, {self.listaCidade}'
