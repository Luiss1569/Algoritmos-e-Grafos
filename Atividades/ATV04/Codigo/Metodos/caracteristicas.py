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
Entrada: Matriz de adjacências  (tipo numpy.ndarray)  ou lista de adjacencia (Dicionario)
Saída: (Booleano) True se simétrica, False se não simétrica
'''
def verSimetria(data):
    for i in range(len(data)):  # Percorre a matriz linha por linha
        for j in range(len(data[0])):  # Percorre a matriz coluna por coluna
            if data[i][j] != data[j][
                i]:  # Se a célula M[i][j] for diferente da célula M[j][i] a matriz não é simétrica
                return False  # Retorna falso
    return True  # Caso n entre no if do for retorna verdadeiro


''' Função para verificar se existe arestas múltiplas 
Entrada: Matriz de adjacências  (tipo numpy.ndarray)  ou lista de adjacencia (Dicionario)
Saída: (Booleano) True se existir arestas múltiplas, False se não existir'''
def verArestaMultiplas(data):
    for i in range(len(data)):  # Percorre a matriz linha por linha
        for j in range(len(data[0])):  # Percorre a matriz coluna por coluna
            if data[i][j] > 1:  # Se a célula M[i][j] for maior que 1 existe uma ou mais arestas
                return True  # Retorna verdadeiro
    return False  # Caso n entre no if do for retorna falso


'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray) ou lista de adjacencia (Dicionario), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(data, vi, vj):
    if type(data) == dict:  # Se a matriz for um dicionário
        if vi in data and vj in data[vi]:
            verticesAdjacentes = True
        else:
            verticesAdjacentes = False
    else:
        if data[vi][vj] > 0:  # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
            verticesAdjacentes = True
        else:
            verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


'''Função para verificar as propriedades do grano e retornar o tipo do grafo
Entrada: Matriz de adjacências  (tipo numpy.ndarray) ou lista de adjacencias e se deseja imprimir o tipo do grafo (default True)
Saída: (Integer) 0 - Simples; 1 - Digrafo; 2 - Multigrafo; 3 - Pseudografo; 4 - Multigrafo Dirigido'''
def tipoGrafo(data, printa=True):
    arestaDirigida = False  # Inicializa a variável que verifica se existe aresta dirigida
    arestaMultiplas = False  # Inicializa a variável que verifica se existe aresta múltiplas
    lacos = False  # Inicializa a variável que verifica se existe laços

    if type(data) is dict:  # Se a matriz for um dicionário, ela e uma lista de adjacências
        for i in data:  # Percorre a matriz linha por linha
            for j in range(len(data[i])):  # Percorre a matriz coluna por coluna
                if data[i][j] in data[i][
                                     j + 1:]:  # Se a célula M[i][j] for igual a alguma célula M[i][j:] existe uma aresta múltipla
                    arestaMultiplas = True
                if i not in data[
                    data[i][j]]:  # Se a célula M[i][j] não estiver na lista M[M[i][j]] existe uma aresta dirigida
                    arestaDirigida = True
                if i in data[i]:
                    lacos = True
    else:  # Se a matriz não for um dicionário, ela e uma matriz de adjacências
        if sum(np.diagonal(data)) > 0:  # Se a soma da diagonal principal for maior que 0 existe laços
            lacos = True  # Atribui True a variável lacos

        if verSimetria(data) == False:  # Se a matriz não for simétrica
            arestaDirigida = True  # Atribui True a variável arestaDirigida

        if verArestaMultiplas(data):  # Se a matriz possuir arestas múltiplas
            arestaMultiplas = True  # Atribui True a variável arestaMultiplas

    if not arestaDirigida and not arestaMultiplas and not lacos:  # Se não existir aresta dirigida, aresta múltiplas e laços
        tipo = tipos.simples  # Atribui o tipo simples
    elif arestaDirigida and not arestaMultiplas and lacos:  # Se existir aresta dirigida, não existir aresta múltiplas e existir laços
        tipo = tipos.digrafo  # Atribui o tipo digrafo
    elif not arestaDirigida and arestaMultiplas and not lacos:  # Se não existir aresta dirigida, existir aresta múltiplas e não existir laços
        tipo = tipos.multigrafo  # Atribui o tipo multigrafo
    elif not arestaDirigida and arestaMultiplas and lacos:  # Se não existir aresta dirigida, existir aresta múltiplas e existir laços
        tipo = tipos.pseudografo  # Atribui o tipo pseudografo
    else:
        tipo = tipos.multigrafo_dirigido  # Atribui o tipo multigrafo dirigido

    if printa:  # Se o parâmetro printa for True
        print("Tipo do grafo:", tipo.name)  # Imprime o nome do tipo do grafo

    return tipo.value  # Retorna o valor do tipo do grafo


'''Função para calcular a densidade do grafo
Entrada: Matriz de adjacências  (tipo numpy.ndarray)  ou lista de adjacencia (Dicionario)
Saída: (Float) Densidade do grafo'''
def calcDensidade(data):
    tipo = tipoGrafo(data, False)  # Verifica o tipo do grafo

    if type(data) is dict:  # Se a matriz for um dicionário, ela e uma lista de adjacências
        vertices = len(data)  # Atribui o número de vértices a uma variável
        arestas = 0  # Inicializa a variável que armazena o número de arestas
        for i in range(len(data)):  # Percorre a matriz linha por linha
            arestas += len(data[i])  # Soma o número de arestas
    else:
        vertices = len(data)  # Quantidade de vértices
        arestas = 0  # Inicializa a quantidade de arestas
        for i in range(0, vertices):  # Percorre a matriz linha por linha
            for j in range(0, vertices):  # Percorre a matriz coluna por coluna
                if data[i][j] > 0:  # Se a célula M[i][j] for maior que 0 existe uma ou mais arestas
                    arestas += data[i][j]  # Incrementa a quantidade de arestas

    if tipo == tipos.digrafo.value or tipo == tipos.multigrafo_dirigido.value:  # Se o grafo for dirigido
        arestas = arestas / 2  # Divide a quantidade de arestas por 2

    densidade = arestas / (vertices * (vertices - 1))  # Calcula a densidade do grafo
    densidade = float("{:.3f}".format(densidade))  # Arredonda a densidade para 3 casas decimais

    print("Densidade do grafo:", densidade)  # Imprime a densidade do grafo
    return densidade  # Retorna a densidade do grafo


'''Funcão para inserir uma aresta no grafo
Entrada: Matriz de adjacências  (tipo numpy.ndarray)  ou lista de adjacencia (Dicionario), vértice de origem (Integer), vértice de destino (Integer)
Saída: Matriz de adjacências  (tipo numpy.ndarray)'''
def insereAresta(data, vi, vj):
    tipo = tipoGrafo(data, False)  # Verifica o tipo do grafo

    if type(data) is dict:  # Se a matriz for um dicionário, ela e uma lista de adjacências
        if vi not in data or vj not in data:  # Se o vértice de origem ou o vértice de destino não existir
            print("Vértice de origem não existe")
            return data  # Retorna a matriz sem alterações
        if tipo == tipos.digrafo.value or tipo == tipos.multigrafo_dirigido.value:
            data[vi].append(vj)  # Adiciona o vértice de destino na lista de adjacências do vértice de origem
        else:
            data[vi].append(vj)
            data[vj].append(vi)
    else:
        if (vi < 0 or vi > len(data)) or (vj < 0 or vj > len(data)):  # Se os vértices forem inválidos
            print("Vértices inválidos")  # Imprime mensagem de erro
            return data  # Retorna a matriz sem alterações

        if tipo == tipos.digrafo or tipo == tipos.multigrafo_dirigido:  # Se o grafo for dirigido
            data[vi][vj] += 1  # Incrementa a quantidade de arestas
        else:
            data[vi][vj] += 1  # Incrementa a quantidade de arestas
            data[vj][vi] += 1  # Incrementa a quantidade de arestas (aresta simétrica)

    return data  # Retorna a matriz de adjacências


'''Função para inserir um vértice no grafo
Entrada: Matriz de adjacências  ou lista de adjacencia (Dicionario), vértice a ser inserido (Integer)
Saída: Matriz de adjacências'''
def insereVertice(data, v):
    if type(data) is dict:  # Se a matriz for um dicionário, ela e uma lista de adjacências
        if v not in data:
            data[v] = []
        else:
            print("Vértice já existe")
    else:
        n = len(data)  # Quantidade de vértices

        if v < n:  # Se o vértice a ser inserido for menor que a quantidade de vértices
            print("Vertice já existe")  # Imprime que o vértice já existe
            return False  # Retorna falso

        data = np.insert(data, n, 0, axis=0)  # Insere uma linha na matriz
        data = np.insert(data, n, 0, axis=1)  # Insere uma coluna na matriz

    return data  # Retorna a matriz de adjacências


'''Função para remover uma aresta do grafo
Entrada: Matriz de adjacências  ou lista de adjacencia (Dicionario), vértice de origem (Integer), vértice de destino (Integer)
Saída: Matriz de adjacências'''
def removeAresta(data, vi, vj):
    tipo = tipoGrafo(data, False)  # Verifica o tipo do grafo

    if type(data) is dict:  # Se a matriz for um dicionário, ela e uma lista de adjacências
        if vi not in data or vj not in data:
            print("Vértice de origem não existe")
            return data
        if tipo == tipos.digrafo.value or tipo == tipos.multigrafo_dirigido.value:
            if vj in data[vi]:
                data[vi].remove(vj)
        else:
            data[vi].remove(vj)
            data[vj].remove(vi)
    else:
        if tipo == tipos.simples.value:  # Se o grafo for simples
            data[vi][vj] = 0  # Remove a aresta
            data[vj][vi] = 0  # Remove a aresta (aresta simétrica)
        elif tipo == tipos.digrafo.value or tipo == tipos.multigrafo_dirigido.value:  # Se o grafo for dirigido
            data[vi][vj] = 0  # Remove a aresta
        else:
            data[vi][vj] -= 1  # Decrementa a quantidade de arestas
            data[vj][vi] -= 1  # Decrementa a quantidade de arestas (aresta simétrica)

    return data  # Retorna a matriz de adjacências


'''Função para remover um vértice do grafo
Entrada: Matriz de adjacências  ou lista de adjacencia (Dicionario), vértice a ser removido (Integer)
Saída: Matriz de adjacências'''
def removeVertice(data, v):
    n = len(data)  # Quantidade de vértices

    if type(data) is dict:  # Se a matriz for um dicionário, ela e uma lista de adjacências
        if v not in data:
            print("Vértice não existe")
            return data
        else:
            del data[v]
            for i in data:
                if v in data[i]:
                    data[i].remove(v)
    else:
        if v >= n:
            print("Vertice não existe")  # Se o vértice a ser removido for maior ou igual a quantidade de vértices
            return False  # Retorna falso

        data = np.delete(data, v, axis=0)  # Remove a linha da matriz
        data = np.delete(data, v, axis=1)  # Remove a coluna da matriz

    return data  # Retorna a matriz de adjacências
