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

    #Condições para identificação dos grafos
    diagonalEhZerada = True
    contemParalelas = False
    ehSimetrica = True

    #Encontrando a quantidade de vértices para percorrer a matriz de adjacência corretamente
    qtdVertices = np.shape(matriz)[0]

    for vi in range(0, qtdVertices):
        for vj in range(vi + 1, qtdVertices):

            #Verifica se é uma posição da diagonal
            if vi == vj:

                #Verifica se uma posição da diagonal é zerada
                if matriz[vi][vj] != 0:
                    diagonalEhZerada = False

            #Verifica se a matriz contém arestas paralelas
            if matriz[vi][vj] == 2:
                contemParalelas = True

            #Verifica se a matriz é simétrica ou assimétrica
            if matriz[vi][vj] != matriz[vj][vi]:
                ehSimetrica = False

    #Condicionais para identificar o grafo
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

    #Verificando o tipo do grafo
    tipoGrafo = self.tipoGrafo(matriz)

    #Contando vértices
    qtdVertices = np.shape(matriz)[0]

    arestas=0

    #Contando arestas para a fórmula
    for vi in range(0, qtdVertices):
        for vj in range(vi + 1, qtdVertices):
            if matriz[vi][vj] == 1:
                arestas+=1

    #Executando a fórmula baseado no tipo do grafo
    if tipoGrafo == 0:
        return (2 * arestas) / (qtdVertices * (qtdVertices - 1))

    if tipoGrafo == 1:
        return arestas / (qtdVertices * (qtdVertices - 1))

def insereAresta(self, matriz, vi, vj):
    print("Inserindo aresta...")
    tipoGrafo = self.tipoGrafo(matriz)

    #Condicional baseada no tipo do grafo, para manter a simetria em grafos não-dirigidos
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

    #Criando uma nova matriz de zeros, com as dimensões da anterior + 1
    novaMatriz = numpy.zeros((shape[0] + 1, shape[1] + 1))

    qtdVertices = np.shape(matriz)[0]

    #Transferindo os valores da matriz antiga para a nova
    for vi in range(0, qtdVertices):
        for vj in range(0, qtdVertices):
            novaMatriz[vi][vj] = matriz[vi][vj] #a nova matriz recebe os valores da matriz antiga

    #Retornando a nova matriz
    return novaMatriz

#Remove aresta: Remove uma aresta do grafo considerando o par de vértices vi e vj.
def removeAresta(self, matriz, vi, vj):
    tipoGrafo = self.tipoGrafo(matriz)
    print("Removendo aresta...")

    #Condicional baseada no tipo do grafo, para manter a simetria em grafos não-dirigidos
    if tipoGrafo == 1:
        matriz[vi][vj] = 0
    else:
        matriz[vi][vj] = 0
        matriz[vj][vi] = 0

    return matriz

#Remove vértice: Remove um vértice do grafo.
def removeVertice(matriz, vi):
    pass







