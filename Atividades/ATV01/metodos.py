import numpy as np

def salvar_arquivo(nome_arquivo, conteudo):
    caminho = f'./{nome_arquivo}'
    with open(caminho, 'a') as arquivo:
        arquivo.write(conteudo)


def criar_matriz(nome_arquivo):
    caminho = f'./dados/{nome_arquivo}.txt'

    with open(caminho, 'r') as arquivo:
        data = np.loadtxt(arquivo, dtype=int, delimiter=' ')

    return data
