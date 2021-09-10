import math

INFINITY = math.inf


class Grafo:
    listaDeAdjacencias = {}
    vertices_abertos = []
    vertices_fechados = []
    rot = []
    dt = []

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

    def fecha_o_vertice(self, vrt):
        self.vertices_abertos[vrt] = False

    # adiciona o vertice no conjunto dos fechados
    def adiciona_vertice_aos_fechados(self, vrt):
        self.vertices_fechados.append(vrt)

    def vertice_esta_aberto(self, c):
        return self.vertices_abertos[c]

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
            self.listaDeAdjacencias.update({origem: adj_nova})
            if self.get_b() == 0:
                adj_nova_reciproca = [(origem, peso)]
                if destino in self.listaDeAdjacencias:
                    adj_existentes = self.listaDeAdjacencias.get(aresta.get_destino())
                    self.listaDeAdjacencias.update({destino: (adj_existentes + adj_nova_reciproca)})
                else:  # se destino não estiver lá, é só acrescentar normal
                    self.listaDeAdjacencias.update({destino: adj_nova_reciproca})

    def dijkstra(self, vertice_inicial):
        # Inicialização
        self.vertices_abertos.append(None)  # invalida vertices_abertos[0]
        self.dt.append(INFINITY)  # invalida(dt[0]).
        self.rot.append(-1)  # invalida (rot[0])
        for v in range(0, n):
            self.vertices_abertos.append(True)
            self.dt.append(INFINITY)
            self.rot.append(0)
        self.dt[vertice_inicial.get_indice()] = 0
        # Início do algortimo
        while len(self.vertices_fechados) != self.__n:
            vertice_com_menor_dt = self.encontra_vertice_com_menor_dt_entre_os_abertos()
            self.fecha_o_vertice(vertice_com_menor_dt)
            self.adiciona_vertice_aos_fechados(vertice_com_menor_dt)
            # self.vertices_abertos.pop(v)  # tira o vértice v dos abertos.
            vizinhos_abertos_do_vertice = self.obter_vizinhos_abertos_de(vertice_com_menor_dt)
            if vizinhos_abertos_do_vertice is not None:
                for vizinho, peso in vizinhos_abertos_do_vertice:
                    if self.dt[vertice_com_menor_dt] + peso < self.dt[vizinho.get_indice()]:
                        self.dt[vizinho.get_indice()] = self.dt[vertice_com_menor_dt] + peso
                        self.rot[vizinho.get_indice()] = vertice_com_menor_dt

    # olha as distancias calculadas de todos os vertices que estão abertos
    def encontra_vertice_com_menor_dt_entre_os_abertos(self):
        dt_dos_abertos = []
        for v in range(0, self.__n + 1):  # pega o dt de todos os vertices que estao abertos
            if self.vertices_abertos[v]:
                dt_dos_abertos.append(self.dt[v])  # e armazena o dt deles em dt_dos_abertos
        return self.dt.index(min(dt_dos_abertos))  # pega o indice do vertice com menor dt

    def obter_vizinhos_abertos_de(self, v):
        vizinhos_abertos_de_v = []
        adjacencias_do_vertice = self.obter_adjacencias(Vertice(v))
        # print(f'Adjacencias de {v}: {adjacencias_do_vertice}')
        if adjacencias_do_vertice is None:
            return None
        for v, p in adjacencias_do_vertice:
            if self.vertice_esta_aberto(v.get_indice()):
                vizinhos_abertos_de_v.append((v, p))
        return vizinhos_abertos_de_v

    def obter_adjacencias(self, vertice):
        return self.listaDeAdjacencias.get(vertice)

    def resposta_dijkstra_formatada(self):
        vertice = 1
        while vertice <= self.__n:
            if self.rot[vertice] == 0:  # origem
                vertice += 1
                continue
            vertice_de_destino = vertice
            #  compondo a estrutura do menor caminho
            menor_caminho = [vertice_de_destino]
            while vertice_de_destino != 0:  # percorrendo o vetor rot até chegar na origem (de trás para frente)
                vertice_de_destino = self.rot[vertice_de_destino]  # atualiza o vertice de destino com o rot dele
                if vertice_de_destino == 0:  # não insere pois 0 é uma abstração para a origem
                    break
                menor_caminho.append(vertice_de_destino)  # acrescenta o rot dele na estrutura do caminho
            menor_caminho.reverse()
            print(f'{vertice} ({self.dt[vertice]}):', end=' ')
            imprime_menor_caminho_formatado(menor_caminho)
            print('')
            vertice += 1

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

    def imprime_lista_de_adjacencias_de(self, vertice):
        print(f'Adjacencias do vertice {vertice}:')
        for adj, peso in self.listaDeAdjacencias.get(vertice):
            print(f'{adj} , peso: {peso}')

    @classmethod
    def obter_rot(cls):
        return cls.rot


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


def imprime_menor_caminho_formatado(menor_caminho):
    for v in menor_caminho:
        print(f'{v}', end=' ')


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

grafo.dijkstra(Vertice(i))
grafo.resposta_dijkstra_formatada()
