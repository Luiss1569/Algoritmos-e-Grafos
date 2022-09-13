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
    listaAdj = ds.criaListaAdjacencias(instancia)

    print('Matriz de adjacências:')
    print(matriz, '\n') # '\n' para inserir linha em branco ao final do comando

    print('Lista de adjacências:')
    print(listaAdj, '\n')

    G = g.criaGrafo(matriz)
    print("Grafo matriz de adjacencias: ")
    print(G, '\n') # Mostra as características do grafo.
    vis.visualizarGrafo(False, G)  # True para visualização do grafo ou False.

    G = g.criaGrafo(listaAdj)
    print("Grafo da lista adjacências: ")
    print(G, '\n')  # Mostra as características do grafo.
    vis.visualizarGrafo(False, G)  # True para visualização do grafo ou False.

    print("\nVerifica adjacencia pela matriz: ")
    car.verificaAdjacencia(matriz, 0, 1)
    print("Verifica adjacencia pela lista: ")
    car.verificaAdjacencia(listaAdj, 0, 1)

    print("\nTipo do grafo pela matriz: ")
    car.tipoGrafo(matriz)
    print("\nTipo do grafo pela lista: ")
    car.tipoGrafo(listaAdj)

    print("\nDensidade do grafo pela matriz: ")
    car.calcDensidade(matriz)
    print("\nDensidade do grafo pela lista: ")
    car.calcDensidade(listaAdj)

    car.insereVertice(listaAdj, 7)
    car.insereAresta(listaAdj, 0, 7)
    print("\nLista de adjacências após inserção de vértice 7 e aresta (0,7): ")
    print(listaAdj)
    car.removeAresta(listaAdj, 0, 7)
    car.removeVertice(listaAdj, 7)
    print("\nLista de adjacências após remoção de vértice 7 e aresta (0,7): ")
    print(listaAdj)

   #ds.salvaResultado(resultado) # Salva resultado em arquivo

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str(sys.argv[1]))

