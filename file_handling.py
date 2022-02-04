import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, text, a_w):
    with open(file_path, a_w) as file:
        file.write(text)

def rename_file(file_path, new_file_path):
    os.rename(file_path, new_file_path)


