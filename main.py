'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.6

05/09/2022
===================================================='''

from igraph import *
from Inicializacao import (dataSet as ds, grafo as g, visualizacao as vis)
from Metodos import (caracteristicas as car)

'''Core do programa'''
def main(instancia):
    matriz = ds.criaMatrizAdjacencias(instancia)
    print(matriz, '\n') # '\n' para inserir linha em branco ao final do comando

    G = g.criaGrafo(matriz)
    print(G, '\n') # Mostra as características do grafo.

    vis.visualizarGrafo(True, G)  # True para visualização do grafo ou False.
    funcao1 = car.verificaAdjacencia(matriz, 0, 1)

    resultado = [instancia, funcao1] # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado) # Salva resultado em arquivo

    funcao2 = car.tipoGrafo(matriz)
    print("Tipo do grafo: {}".format(funcao2))

    resultado = [instancia, funcao2]  # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado)  # Salva resultado em arquivo

    funcao3 = car.calcDensidade(car, matriz)
    print("Densidade do grafo: {}".format(funcao3))

    resultado = [instancia, funcao3]  # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado)  # Salva resultado em arquivo

    funcao4 = car.insereAresta(car, matriz, 2, 6)
    G = g.criaGrafo(funcao4)
    vis.visualizarGrafo(True, G)

    resultado = [instancia, funcao4]  # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado)  # Salva resultado em arquivo

    funcao5 = car.insereVertice(matriz, 0)
    G = g.criaGrafo(funcao5)
    vis.visualizarGrafo(True, G)

    resultado = [instancia, funcao5]  # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado)  # Salva resultado em arquivo

    funcao6 = car.removeAresta(car, matriz, 0, 1)
    G = g.criaGrafo(funcao6)
    vis.visualizarGrafo(True, G)

    resultado = [instancia, funcao6]  # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado)  # Salva resultado em arquivo

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str('exemplo'))


