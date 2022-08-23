import sys
import metodos as mt
import numpy as np

if __name__ == '__main__':
    for arquivo in sys.argv[1:]:
        matriz = mt.criar_matriz(arquivo)
        print(f'{"-"*3} {arquivo} {"-"*3}')
        print(matriz)

        resultado = f'{arquivo} {str(matriz.shape)}'

        print(f'Resultado: {resultado}\n')

        mt.salvar_arquivo('resultado.txt', resultado)