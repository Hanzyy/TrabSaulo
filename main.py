from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator
from array_stack import ArrayStack
from array_queue_new import ArrayQueue
from listaDuplamenteEncadeadaComIteradorFinal_Solucao import DoublyLinkedListIterator
from objeto import Objeto
from manutencao import Manutencao


def rodoviasCidade(nomeCidade, lstRodovias):
    lstRodovias.first_Node()        #Coloca o iterador no primeiro nó
    lst = SinglyLinkedListIterator()        #Cria uma lista de apoio
    while lstRodovias.iterator:     #Enquanto tiver elementos na Lista Simplesmente Encadeada
        lstRodovias.iterator.data.listaCidade.first_Node()      #Pega a data do iterador da lista simplesmente encadeada, que vai para um objeto, onde coloca o iterador da lista duplamente encadeada no primeiro nó
        while lstRodovias.iterator.data.listaCidade.iterator:       #Enquanto tiver elementos na lista Duplamente Encadeada
            if lstRodovias.iterator.data.listaCidade.iterator.data == nomeCidade:      #Verifica quais rodovias passam pela cidade
                lst.addNode(lstRodovias.iterator.data.rodovia)      #Adiciona as cidades à lista de apoio
            lstRodovias.iterator.data.listaCidade.nextNode()        #Avança para o próximo nó na lista Duplamente Encadeada
        lstRodovias.nextNode()      #Avança para o próximo nó na lista Simplesmente Encadeada
    return lst      #Retorna a lista de rodovias que passam por aquela cidade


def programarManutencao(fila:ArrayQueue, novaManutencao:Manutencao):
    fila.enqueue(novaManutencao)    #Adiciona uma manutenção à fila
    return fila


def registrarHistoricoManutencoes(fila:ArrayQueue, pilha:ArrayStack):
    pilha.push(fila.dequeue())      #Remove a primeira manutenção e coloca na pilha
    return pilha

def registrarLista(filename):
    rodovias = SinglyLinkedListIterator()   # Declara a lista de rodovias
    with open(filename, 'r') as file:   # Lê o arquivo que guarda as listas
        for linha in file:
            data = linha.split()    # Para cada linha no arquivo separa as palavras por espaços
            nomeRodovia = data[0]   # Designa a primeira palavra da lista para o campo rodovia
            cidades = DoublyLinkedListIterator()
            i = 1
            while i < len(data):        # Enquanto o tamanho da variável de apoio i é menor que a posição da data
                a = data[i]
                cidades.addNode(a)      # Adiciona a data a lista cidade
                i+=1
            rodovia = Objeto(nomeRodovia, cidades)  # Instancia a classe objeto
            rodovias.addNode(rodovia)       # Adiciona esse objeto na lista de rodovias
    return rodovias     # retorna rodovias


if __name__ == '__main__':

    lst = registrarLista("cidades.txt")
    lst.printLista()

    print(lst.iterator.data.listaCidade.iterator.data)
    lst.iterator.data.listaCidade.first_Node()
    print(lst.iterator.data.listaCidade.iterator.data)


    """lstBR101 = DoublyLinkedListIterator()
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
    fila.printFila()"""
