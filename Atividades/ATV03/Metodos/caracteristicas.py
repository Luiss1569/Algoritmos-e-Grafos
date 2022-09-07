'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

import numpy as np
from enum import Enum

''''  Enum para tipos de grafos e seus respectivos valores '''
class tipos(Enum):
    simples = 0
    digrafo = 1
    multigrafo = 2
    pseudografo = 3
    multigrafo_dirigido = 4

''' Função verificar se existe uma simetria na matriz de adjacências 
Entrada: Matriz de adjacências
Saída: (Booleano) True se simétrica, False se não simétrica
'''
def verSimetria(matriz):
    for i in range(len(matriz)): # Percorre a matriz linha por linha
        for j in range(len(matriz[0])): # Percorre a matriz coluna por coluna
            if matriz[i][j] != matriz[j][i]: # Se a célula M[i][j] for diferente da célula M[j][i] a matriz não é simétrica
                return False # Retorna falso
    return True # Caso n entre no if do for retorna verdadeiro

''' Função para verificar se existe arestas múltiplas 
Entrada: Matriz de adjacências
Saída: (Booleano) True se existir arestas múltiplas, False se não existir'''
def verArestaMultiplas(matriz):
    for i in range(len(matriz)): # Percorre a matriz linha por linha
        for j in range(len(matriz[0])): # Percorre a matriz coluna por coluna
            if matriz[i][j] > 1: # Se a célula M[i][j] for maior que 1 existe uma ou mais arestas
                return True # Retorna verdadeiro
    return False # Caso n entre no if do for retorna falso


'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0:  # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

'''Função para verificar as propriedades do grano e retornar o tipo do grafo
Entrada: Matriz de adjacências e se deseja imprimir o tipo do grafo (default True)
Saída: (Integer) 0 - Simples; 1 - Digrafo; 2 - Multigrafo; 3 - Pseudografo; 4 - Multigrafo Dirigido'''
def tipoGrafo(matriz, printa=True):
    arestaDirigida = False # Inicializa a variável que verifica se existe aresta dirigida
    arestaMultiplas = False # Inicializa a variável que verifica se existe aresta múltiplas
    lacos = False # Inicializa a variável que verifica se existe laços

    if sum(np.diagonal(matriz)) > 0: # Se a soma da diagonal principal for maior que 0 existe laços
        lacos = True # Atribui True a variável lacos

    if verSimetria(matriz) == False: # Se a matriz não for simétrica
        arestaDirigida = True # Atribui True a variável arestaDirigida

    if verArestaMultiplas(matriz): # Se a matriz possuir arestas múltiplas
        arestaMultiplas = True # Atribui True a variável arestaMultiplas

    if not arestaDirigida and not arestaMultiplas and not lacos: # Se não existir aresta dirigida, aresta múltiplas e laços
        tipo = tipos.simples # Atribui o tipo simples
    elif arestaDirigida and not arestaMultiplas and lacos: # Se existir aresta dirigida, não existir aresta múltiplas e existir laços
        tipo = tipos.digrafo # Atribui o tipo digrafo
    elif not arestaDirigida and arestaMultiplas and not lacos: # Se não existir aresta dirigida, existir aresta múltiplas e não existir laços
        tipo = tipos.multigrafo # Atribui o tipo multigrafo
    elif not arestaDirigida and arestaMultiplas and lacos: # Se não existir aresta dirigida, existir aresta múltiplas e existir laços
        tipo = tipos.pseudografo # Atribui o tipo pseudografo
    else:
        tipo = tipos.multigrafo_dirigido # Atribui o tipo multigrafo dirigido

    if printa: # Se o parâmetro printa for True
        print("Tipo do grafo:", tipo.name) # Imprime o nome do tipo do grafo

    return tipo.value # Retorna o valor do tipo do grafo

'''Função para calcular a densidade do grafo
Entrada: Matriz de adjacências
Saída: (Float) Densidade do grafo'''
def calcDensidade(matriz):
    tipo = tipoGrafo(matriz, False) # Verifica o tipo do grafo
    vertices = len(matriz) # Quantidade de vértices
    arestas = 0 # Inicializa a quantidade de arestas
    for i in range(0, vertices): # Percorre a matriz linha por linha
        for j in range(0, vertices): # Percorre a matriz coluna por coluna
            if matriz[i][j] > 0: # Se a célula M[i][j] for maior que 0 existe uma ou mais arestas
                arestas += matriz[i][j] # Incrementa a quantidade de arestas

    if tipo == tipos.digrafo.value: # Se o grafo for dirigido
        arestas = arestas / 2 # Divide a quantidade de arestas por 2

    densidade = arestas / (vertices * (vertices - 1))  # Calcula a densidade do grafo
    densidade = float("{:.3f}".format(densidade)) # Arredonda a densidade para 3 casas decimais

    print("Densidade do grafo:", densidade) # Imprime a densidade do grafo
    return densidade # Retorna a densidade do grafo

'''Funcão para inserir uma aresta no grafo
Entrada: Matriz de adjacências, vértice de origem (Integer), vértice de destino (Integer)
Saída: Matriz de adjacências'''
def insereAresta(matriz, vi, vj):
    tipo = tipoGrafo(matriz, False) # Verifica o tipo do grafo

    if tipo == tipos.digrafo or tipo == tipos.multigrafo_dirigido: # Se o grafo for dirigido
        matriz[vi][vj] += 1 # Incrementa a quantidade de arestas
    else:
        matriz[vi][vj] += 1 # Incrementa a quantidade de arestas
        matriz[vj][vi] += 1 # Incrementa a quantidade de arestas (aresta simétrica)

    return matriz # Retorna a matriz de adjacências

'''Função para inserir um vértice no grafo
Entrada: Matriz de adjacências, vértice a ser inserido (Integer)
Saída: Matriz de adjacências'''
def insereVertice(matriz, v):
    n = len(matriz) # Quantidade de vértices

    if v < n: # Se o vértice a ser inserido for menor que a quantidade de vértices
        print("Vertice já existe") # Imprime que o vértice já existe
        return False # Retorna falso

    matriz = np.insert(matriz, n, 0, axis=0) # Insere uma linha na matriz
    matriz = np.insert(matriz, n, 0, axis=1) # Insere uma coluna na matriz

    return matriz # Retorna a matriz de adjacências

'''Função para remover uma aresta do grafo
Entrada: Matriz de adjacências, vértice de origem (Integer), vértice de destino (Integer)
Saída: Matriz de adjacências'''
def removeAresta(matriz, vi, vj):
    tipo = tipoGrafo(matriz, False) # Verifica o tipo do grafo

    if tipo == tipos.simples.value: # Se o grafo for simples
        matriz[vi][vj] = 0 # Remove a aresta
        matriz[vj][vi] = 0 # Remove a aresta (aresta simétrica)
    elif tipo == tipos.digrafo.value or tipo == tipos.multigrafo_dirigido.value:  # Se o grafo for dirigido
        matriz[vi][vj] = 0 # Remove a aresta
    else:
        matriz[vi][vj] -= 1 # Decrementa a quantidade de arestas
        matriz[vj][vi] -= 1 # Decrementa a quantidade de arestas (aresta simétrica)

    return matriz # Retorna a matriz de adjacências

'''Função para remover um vértice do grafo
Entrada: Matriz de adjacências, vértice a ser removido (Integer)
Saída: Matriz de adjacências'''
def removeVertice(matriz, v):
    n = len(matriz) # Quantidade de vértices

    if v >= n:
        print("Vertice não existe") # Se o vértice a ser removido for maior ou igual a quantidade de vértices
        return False # Retorna falso

    matriz = np.delete(matriz, v, axis=0) # Remove a linha da matriz
    matriz = np.delete(matriz, v, axis=1) # Remove a coluna da matriz
    return matriz # Retorna a matriz de adjacências
