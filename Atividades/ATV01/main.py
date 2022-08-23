import sys
import metodos as mt
import numpy as np

if __name__ == '__main__':
    # A loop that iterates over the files passed as arguments to the program.
    for file in sys.argv[1:]:
        
        # Creating a matrix from the file.
        matriz = mt.create_grid(file)
        
        # Printing a line of dashes before and after the file name.
        print(f'{"-"*3} {file} {"-"*3}')
        
        # Printing the matrix.
        print(matriz)

        # Creating a string with the name of the file and the shape of the matrix.
        result = f'{file} {str(matriz.shape)}\n'

        # Printing the result of the file and the shape of the matrix.
        print(f'Resultado: {result}')

        # Saving the result of the file and the shape of the matrix in a file
        # called resultado.txt.
        mt.save_file('resultado.txt', result)