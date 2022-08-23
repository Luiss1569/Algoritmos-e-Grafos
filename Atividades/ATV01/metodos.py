import numpy as np

# Luis Ricardo Albano Santos - 2021031844

"""
    > The function takes in two arguments, a file name and content, and writes the
    content to the file
    
    :param file_name: The name of the file you want to save
    :param content: the content to be written to the file
"""
def save_file(file_name, content):
    file_path = f'./{file_name}'
    with open(file_path, 'a') as file:
        file.write(content)
    file.close()

"""
    > It reads the file and returns a numpy array
    
    :param file_name: the name of the file that contains the grid
    :return: A matrix with the values of the file.
"""
def create_grid(file_name):
    file_path = f'./dados/{file_name}.txt'

    with open(file_path, 'r') as file:
        data = np.loadtxt(file, dtype=int, delimiter=' ')

    return data
