'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''
import numpy
import numpy as np

#Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

#Descrição: Retorna o tipo do grafo representado por uma dada matriz de adjacências.
def tipoGrafo(matriz):

    diagonalEhZerada = True
    contemParalelas = False
    ehSimetrica = True

    qtdVertices = np.shape(matriz)[0]

    for vi in range(0, qtdVertices):
        for vj in range(vi + 1, qtdVertices):

            if vi == vj:
                if matriz[vi][vj] != 0:
                    diagonalEhZerada = False

            if matriz[vi][vj] == 2:
                contemParalelas = True

            if matriz[vi][vj] != matriz[vj][vi]:
                ehSimetrica = False

    if diagonalEhZerada and not contemParalelas and ehSimetrica: #SIMPLES
        return 0
    if diagonalEhZerada and not contemParalelas and not ehSimetrica: #DIGRAFO
        return 1
    if diagonalEhZerada and contemParalelas: #MULTIGRAFO
        return 2
    if not diagonalEhZerada and contemParalelas: #PSEUDOGRAFO
        return 3

#Descrição: Retorna o valor da densidade do grafo.
def calcDensidade(self, matriz):

    tipoGrafo = self.tipoGrafo(matriz)
    qtdVertices = np.shape(matriz)[0]

    arestas=0
    for vi in range(0, qtdVertices):
        for vj in range(vi + 1, qtdVertices):
            if matriz[vi][vj] == 1:
                arestas+=1

    if tipoGrafo == 0:
        return (2 * arestas) / (qtdVertices * (qtdVertices - 1))

    if tipoGrafo == 1:
        return arestas / (qtdVertices * (qtdVertices - 1))

def insereAresta(self, matriz, vi, vj):
    print("Inserindo aresta...")
    tipoGrafo = self.tipoGrafo(matriz)
    if tipoGrafo == 1:
        matriz[vi][vj] = 1
    else:
        matriz[vi][vj] = 1
        matriz[vj][vi] = 1

    return matriz

#Insere vértice: Insere um vértice no grafo.
def insereVertice(matriz, vi):
    print("Inserindo vértice...")
    shape = matriz.shape
    novaMatriz = numpy.zeros((shape[0] + 1, shape[1] + 1))

    qtdVertices = np.shape(matriz)[0]
    for vi in range(0, qtdVertices):
        for vj in range(0, qtdVertices):
            novaMatriz[vi][vj] = matriz[vi][vj] #a nova matriz recebe os valores da matriz antiga

    return novaMatriz

#Remove aresta: Remove uma aresta do grafo considerando o par de vértices vi e vj.
def removeAresta(self, matriz, vi, vj):
    tipoGrafo = self.tipoGrafo(matriz)
    print("Removendo aresta...")

    if tipoGrafo == 1:
        matriz[vi][vj] = 0
    else:
        matriz[vi][vj] = 0
        matriz[vj][vi] = 0

    return matriz

#Remove vértice: Remove um vértice do grafo.
def removeVertice(matriz, vi):
    pass







