flag = None
grafo = []

n = int(input())
m = int(input())
b = int(input())

# criação da matriz de pesos de ordem N
for i in range(0, n):
    grafo.append([None])
    for j in range(0, n - 1):
        grafo[i].append(None)

# Leitura das m linhas
for linha in range(0, m):
    origem = int(input())
    destino = int(input())
    peso = int(input())
    # Inserindo na matriz
    grafo[origem - 1][destino - 1] = peso
    # GND
    if b == 0:
        grafo[destino - 1][origem - 1] = peso

if b == 1:
    flag = "DIRECIONADO"
elif b == 0:
    flag = "NÃO DIRECIONADO"

print(f'{n} {m} {flag}')

for origem in range(0, n):
    for destino in range(0, n):
        if grafo[origem][destino]:
            print(f'{origem + 1} {destino + 1} {grafo[origem][destino]}')

