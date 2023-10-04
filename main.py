from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator
from array_stack import ArrayStack
from array_queue_new import ArrayQueue
from listaDuplamenteEncadeadaComIteradorFinal_Solucao import DoublyLinkedListIterator
from objeto import Objeto


def rodoviasCidade(nomeCidade, lstRodovias):
    lstRodovias.first_Node()
    lst = SinglyLinkedListIterator()
    while lstRodovias.iterator:
        lstRodovias.iterator.data.listaCidade.first_Node()
        while lstRodovias.iterator.data.listaCidade.iterator:
            if lstRodovias.iterator.data.listaCidade.iterator.data == nomeCidade:
                lst.addNode(lstRodovias.iterator.data.rodovia)
            lstRodovias.iterator.data.listaCidade.nextNode()
        lstRodovias.nextNode()
    return lst























if __name__ == '__main__':


    lstBR101 = DoublyLinkedListIterator()
    lstBR101.first_Node()
    lstBR101.addNode("Vitória")
    lstBR101.addNode("Serra")
    lstBR101.addNode("Cariacica")
    objeto1 = Objeto("BR-101", lstBR101)


    lstRodoviaDoSol = DoublyLinkedListIterator()
    lstRodoviaDoSol.addNode("Vila Velha")
    lstRodoviaDoSol.addNode("Guarapari")
    lstRodoviaDoSol.addNode("Vitória")
    objeto2 = Objeto("Rodovia Do Sol", lstRodoviaDoSol)

    lstBR262 = DoublyLinkedListIterator()
    lstBR262.addNode("Venda Nova do Imigrante")
    lstBR262.addNode("Vitória")
    lstBR262.addNode("Guaçuí")
    lstBR262.addNode("Vila Velha")
    objeto3 = Objeto("BR-262", lstBR262)


    #lstRodoviaDoSol.printLista()

    listaRodovias = SinglyLinkedListIterator()
    listaRodovias.addNode(objeto1)
    listaRodovias.addNode(objeto2)
    listaRodovias.addNode(objeto3)

    rodo = rodoviasCidade("Vitória", listaRodovias)
    rodo.printLista()


    asfaltar = Manutencao("BR-101", "10/10/2023", "Asfaltar")
    pavimentar = Manutencao("Rodovia do Sol", "05/03/2024", "Pavimentar")
    fila = ArrayQueue()

    fila.enqueue(asfaltar)
    fila.enqueue(pavimentar)
    fila.printFila()
