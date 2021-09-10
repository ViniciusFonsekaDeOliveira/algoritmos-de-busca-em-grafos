# definições
class Grafo:
    listaDeAdjacencias = {}
    vertices_nao_visitados = []
    arestas_nao_exploradas = {}

    def __init__(self, n, m, b):
        self.__n = n
        self.__m = m
        self.__b = b
        #  invalidando o indice 0
        self.vertices_nao_visitados.append(None)
        for i in range(0, n):
            self.vertices_nao_visitados.append(True)

    def get_n(self):
        return self.__n

    def get_m(self):
        return self.__m

    def get_b(self):
        return self.__b

    def marcar_como_visitado(self, vrt):
        self.vertices_nao_visitados[vrt] = False

    def existe_vertice_nao_visitado(self, c):
        return self.vertices_nao_visitados[c]

    def adionar_aresta(self, aresta):
        origem = aresta.get_origem()
        destino = aresta.get_destino()
        peso = aresta.get_peso()
        adj_nova = [(destino, peso)]
        if origem in self.listaDeAdjacencias:
            # pega as adjacencias que já estão lá
            adj_existentes = self.listaDeAdjacencias.get(origem)  # da origem
            self.listaDeAdjacencias.update({origem: (adj_existentes + adj_nova)})
            if self.get_b() == 0:
                # acrecentar a origem enquanto adjacencia do destino também
                adj_nova_reciproca = [(origem, peso)]
                if destino in self.listaDeAdjacencias:
                    adj_existentes = self.listaDeAdjacencias.get(aresta.get_destino())  # do destino
                    self.listaDeAdjacencias.update({destino: (adj_existentes + adj_nova_reciproca)})
                else:
                    self.listaDeAdjacencias.update({destino: adj_nova_reciproca})
        else:  # caso origem nao esteja no grafo ainda
            self.arestas_nao_exploradas.update({(origem, destino, peso): True})
            self.listaDeAdjacencias.update({origem: adj_nova})
            if self.get_b() == 0:
                self.arestas_nao_exploradas.update({(destino, origem, peso): True})
                adj_nova_reciproca = [(origem, peso)]
                if destino in self.listaDeAdjacencias:
                    adj_existentes = self.listaDeAdjacencias.get(aresta.get_destino())
                    self.listaDeAdjacencias.update({destino: (adj_existentes + adj_nova_reciproca)})
                else:  # se destino não estiver lá, é só acrescentar normal
                    self.listaDeAdjacencias.update({destino: adj_nova_reciproca})

    def dfs(self, vertice_inicial):
        self.marcar_como_visitado(vertice_inicial.get_indice())
        print(f'{vertice_inicial.get_indice()}', end=' ')
        adjacencias = self.obter_adjacencias(vertice_inicial)
        for (vizinho, peso) in adjacencias:
            if self.existe_vertice_nao_visitado(vizinho.get_indice()):
                self.explorar_aresta(Aresta(vertice_inicial, vizinho, peso))  # explora a aresta
                self.dfs(vizinho)  # chamada recursiva para a função
            else:
                if self.existe_aresta_nao_explorada(Aresta(vertice_inicial, vizinho, peso)):
                    self.explorar_aresta(Aresta(vertice_inicial, vizinho, peso))

    def obter_adjacencias(self, vertice):
        return self.listaDeAdjacencias.get(vertice)

    def explorar_aresta(self, aresta):
        v1 = aresta.get_origem().get_indice
        v2 = aresta.get_destino().get_indice
        p = aresta.get_peso()
        self.arestas_nao_exploradas.update({(v1, v2, p): False})
        if self.get_b() == 0:
            self.arestas_nao_exploradas.update({(v2, v1, p): False})

    def existe_aresta_nao_explorada(self, aresta):
        v1 = aresta.get_origem().get_indice
        v2 = aresta.get_destino().get_indice
        p = aresta.get_peso()
        return self.arestas_nao_exploradas.get((v1, v2, p))

    def imprime_nmb_formatado(self):
        if self.get_b() == 0:
            texto = "NÃO DIRECIONADO"
        else:
            texto = "DIRECIONADO"
        print(f'{self.get_n()} {self.get_m()} {texto}')

    @classmethod
    def imprime_lista_de_adjacencias_formatada(cls):
        for origem in cls.listaDeAdjacencias:
            for (destino, peso, aresta_nao_explorada) in cls.listaDeAdjacencias.get(origem):
                print(f'{origem.get_indice()} {destino.get_indice()} {peso} {aresta_nao_explorada}')

    def imprime_lista_de_adjacencias_de(self, vertice):
        print(f'Adjacencias do vertice {vertice}:')
        for adj, peso, aresta_nao_explorada in self.listaDeAdjacencias.get(vertice):
            print(f'{adj} , peso: {peso}, arestaLivre: {aresta_nao_explorada}')


class Vertice:
    def __init__(self, indice):
        self.__indice = indice
        #  self.__nao_visitado = True

    def __str__(self):  # ensina impressão informal
        return str(self.get_indice())

    def __eq__(self, other):  # ensina comparar igualdade entre objetos desta instancia
        return self.get_indice() == other.get_indice()

    def __hash__(self):  # codigo hash de objetos iguais precisa ser igual pra montar o dicionario corretamente
        return hash((self.get_indice()))

    def get_indice(self):
        return self.__indice


class Aresta:
    def __init__(self, origem, destino, peso):
        self.__origem = origem
        self.__destino = destino
        self.__peso = peso

    def get_origem(self):
        return self.__origem

    def get_destino(self):
        return self.__destino

    def get_peso(self):
        return self.__peso


# Entrada
plinha = input()
elemen = plinha.split(' ')

n = int(elemen.pop(0))
m = int(elemen.pop(0))
b = int(elemen.pop(0))
i = int(elemen.pop(0))

grafo = Grafo(n, m, b)

for mlinha in range(0, m):
    origem_destino_peso = input()
    valores = origem_destino_peso.split(' ')
    origem = int(valores.pop(0))
    destino = int(valores.pop(0))
    peso = int(valores.pop(0))
    grafo.adionar_aresta(Aresta(Vertice(origem), Vertice(destino), peso))

grafo.dfs(Vertice(i))
