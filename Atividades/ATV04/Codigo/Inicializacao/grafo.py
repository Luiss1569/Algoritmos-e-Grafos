'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

grafo - Funções para criação de um objeto grafo da biblioteca iGraph.
Mais informações: https://igraph.org/python/tutorial/latest/tutorial.html

05/09/2022
===================================================='''

import igraph
import numpy as np

'''qrVertices: Função para retornar a quantidade de vértices de um grafo
Entrada: matriz de adjacências (tipo numpy.ndarray) ou lista de adjacências (tipo dict)
Saída: quantidade de vértices (tipo int)'''
def getQtdVertices(matriz):
    if type(matriz) == dict:
        return len(matriz)
    else:
        return np.shape(matriz)[0]
    return 0


'''Cria Grafo: Função para criação de um objeto grafo da biblioteca iGraph a partir de uma matriz de adjacências
Entrada: matriz de adjacências (tipo numpy.ndarray)
Saída: grafo (tipo iGraph)'''
def criaGrafo(matriz):
    qtdVertices = getQtdVertices(matriz)
    grafo = igraph.Graph()  # Cria objeto igraph inicialmente vazio
    grafo.add_vertices(qtdVertices)  # Adiciona vértices ao grafo
    grafo.vs["label"] = range(0, grafo.vcount())  # Define o nome de cada nó como um número inteiro

    if type(matriz) == dict:
        for i in matriz:
            for j in range(len(matriz[i])):
                if i < matriz[i][j]:
                    grafo.add_edge(i, matriz[i][j])
    else:
        for vi in range(0, qtdVertices):  # Para cada vértice vi
            for vj in range(vi + 1, qtdVertices):  # Para cada vértice vj
                controle = matriz[vi][vj]
                while controle > 0:  # Adiciona a quantidade de arestas paralelas ou peso da aresta
                    grafo.add_edges([(vi, vj)])
                    controle -= 1

    return grafo
