flag = None
grafo = {}

n = int(input())
m = int(input())
b = int(input())

for linha in range(0, m):
    origem = int(input())
    destino = int(input())
    peso = int(input())
    if origem in grafo:
        # pega as adj antigas
        adjacenciasDaOrigem = grafo.get(origem)
        # atualiza com as adj novas
        grafo.update({origem: (adjacenciasDaOrigem + [(destino, peso)])})
        # GND precisa atualiza as adj dos destinos com cada uma de suas origens.
        if b == 0:
            if destino in grafo:
                adjacenciasDoDestino = grafo.get(destino)
                grafo.update({destino: (adjacenciasDoDestino + [(origem, peso)])})
            else:
                grafo.update({destino: [(origem, peso)]})

    else:
        grafo.update({origem: [(destino, peso)]})
        # GND
        if b == 0:
            if destino in grafo:
                adjacenciasDoDestino = grafo.get(destino)
                grafo.update({destino: (adjacenciasDoDestino + [(origem, peso)])})
            else:
                grafo.update({destino: [(origem, peso)]})

if b == 1:
    flag = "DIRECIONADO"
elif b == 0:
    flag = "NÃO DIRECIONADO"
# Saída
print(f'{n} {m} {flag}')

for vertice in grafo:
    for (adjacencia, peso) in grafo[vertice]:
        print(f'{vertice} {adjacencia} {peso}')
