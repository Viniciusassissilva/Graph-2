from random import randint
from tqdm import tqdm
import numpy as np
import copy
import time

def lista(arq):

    arq.seek(0)
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    Vertices = int(FirstLine[0])
    Arestas = float(FirstLine[1])
    Arestas = int(Arestas)

    Lista = [[] for x in range(Vertices)]

    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        z = Aresta[2]
        if z[-2:] == "\n":
            z = Aresta[:-2]
        Lista[x].append((y, float(z)))
        Lista[y].append((x, float(z)))

    return Lista

def matriz(arq):

    arq.seek(0)
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    Vertices = int(FirstLine[0])
    Arestas = float(FirstLine[1])
    Arestas = int(Arestas)
    Matriz = [[0 for _ in range(Vertices)] for _ in range(Vertices)]

    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        z = Aresta[2]
        if z[-2:] == "\n":
            z = Aresta[:-2]
        Matriz[x][y] = float(z)
        Matriz[y][x] = float(z)

    return Matriz

def contrutivo(Lista):
    #Vizinho mais proximo
    naovisitados = [x for x in range(len(Lista))]
    vvisitado = [0 for x in range(len(Lista))]

    aux = None
    u = 0
    percuso = []
    percuso.append(u)
    vvisitado[0] = 1
    while len(naovisitados) != 1:
        menor = float('inf')
        for i in Lista[u]:
            if i[1] < menor and vvisitado[i[0]] == 0:
                menor = i[1]
                aux = i[0]
        vvisitado[aux] = 1
        percuso.append(aux)
        naovisitados.remove(u)
        u = aux

    percuso.append(percuso[0])
    return percuso

def refinamento(tempo, percuso, Matriz):
    #2-OPT
    aux1 = []
    aux2 = 0
    tentativa = []
    for _ in tqdm(range(tempo), desc="Refinando...", ascii=False, ncols=75):
        vertice = randint(1, len(percuso) - 2)
        vertice2 = randint(1, len(percuso) - 2)

        if vertice != vertice2 and (vertice, vertice2) not in tentativa:

            tentativa.append((vertice, vertice2))

            aux1 = copy.deepcopy(percuso)
            aux2 = aux1[vertice]
            aux1[vertice] = aux1[vertice2]
            aux1[vertice2] = aux2
            if tamnhanho_percuso(aux1, Matriz) < tamnhanho_percuso(percuso, Matriz):
                percuso = copy.deepcopy(aux1)
                print(tamnhanho_percuso(aux1, Matriz))
                tentativa = []

        time.sleep(0.99)

    return percuso



def tamnhanho_percuso(percurso, Matriz):
    tamanho = 0
    for i in range(len(percurso) - 1):
        x = percurso[i]
        y = percurso[i + 1]
        tamanho = tamanho + Matriz[x][y]
    return tamanho