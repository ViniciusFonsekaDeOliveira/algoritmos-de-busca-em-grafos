# definições das classes
class Grafo:
    listaDeAdjacencias = {}

    def __init__(self, n, m, b):
        self.__n = n
        self.__m = m
        self.__b = b

    def get_n(self):
        return self.__n

    def get_m(self):
        return self.__m

    def get_b(self):
        return self.__b

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
                if destino in self.listaDeAdjacencias:
                    adj_existentes = self.listaDeAdjacencias.get(aresta.get_destino())  # do destino
                    self.listaDeAdjacencias.update({destino: (adj_existentes + [(origem, peso)])})
                else:
                    self.listaDeAdjacencias.update({destino: [(origem, peso)]})
        else:
            self.listaDeAdjacencias.update({origem: [(destino, peso)]})
            if self.get_b() == 0:
                if destino in self.listaDeAdjacencias:
                    adj_existentes = self.listaDeAdjacencias.get(aresta.get_destino())
                    self.listaDeAdjacencias.update({destino: (adj_existentes + [(origem, peso)])})
                else:  # se não estiver lá, é só acrescentar normal
                    self.listaDeAdjacencias.update({destino: [(origem, peso)]})

    def imprime_nmb(self):
        print(f'{self.get_n()} {self.get_m()} {self.get_b()}')

    def imprime_nmb_formatado(self):
        if self.get_b() == 0:
            texto = "NÃO DIRECIONADO"
        else:
            texto = "DIRECIONADO"
        print(f'{self.get_n()} {self.get_m()} {texto}')

    @classmethod
    def imprime_lista_de_adjacencias_formatada(cls):
        for origem in cls.listaDeAdjacencias:
            for (destino, peso) in cls.listaDeAdjacencias.get(origem):
                print(f'{origem.get_indice()} {destino.get_indice()} {peso}')

    def dfs(self, vertice_inicial):
        pass


class Vertice:
    def __init__(self, indice):
        self.__indice = indice
        self.__nao_visitado = True

    def __str__(self):  # ensina impressão informal
        return "Indice: " + str(self.get_indice()) + "|" + "Não-Visitado: " + str(self.get_nao_visitado())

    def __eq__(self, other):  # ensina comparar igualdade entre objetos desta instancia
        return self.get_indice() == other.get_indice()

    def __hash__(self):  # codigo hash de objetos iguais precisa ser igual pra montar o dicionario corretamente
        return hash((self.get_indice()))

    def visitar(self):
        self.__nao_visitado = False

    def get_indice(self):
        return self.__indice

    def get_nao_visitado(self):
        return self.__nao_visitado


class Aresta:
    def __init__(self, origem, destino, peso):
        self.__origem = origem
        self.__destino = destino
        self.__peso = peso
        self.__nao_explorada = True

    def get_origem(self):
        return self.__origem

    def get_destino(self):
        return self.__destino

    def get_peso(self):
        return self.__peso

    def get_nao_explorada(self):
        return self.__nao_explorada

    def explorar(self):
        self.__nao_explorada = False

# Entrada
n = int(input())  # quantidade de vértices
m = int(input())  # quantidade de arestas/arcos
b = int(input())  # valor binário indicando se é direcionado (1) ou GND (0).

grafo = Grafo(n, m, b)

for linha in range(0, m):
    origem = int(input())
    destino = int(input())
    peso = int(input())
    a = Aresta(Vertice(origem), Vertice(destino), peso)
    grafo.adionar_aresta(a)

grafo.imprime_nmb_formatado()
grafo.imprime_lista_de_adjacencias_formatada()
