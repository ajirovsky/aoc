from pathlib import Path

class InputLoader:

    def __init__(self, input_file="", input_folder="inputs"):
        self.input_file = input_file
        self.input_folder = input_folder

    def __enter__(self):
        input_path = f"{self.input_folder}/{self.input_file}"
        self.file = open(input_path, "r")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if line == "":
            raise StopIteration()
        return line[:-1]