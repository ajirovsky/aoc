from abc import abstractmethod
from typing import List
from common.input_loader import InputLoader

def pretty_print(func):
    def wrapper(self, input : str) -> int:
        val = func(self, input)
        print(f"The answer for {self.__class__.__name__} (\"{input}\" file) is: {val}")
        return val
    return wrapper

class Solver:

    @abstractmethod
    def solve_first(self, input_name : str) -> int:
        pass

    @abstractmethod
    def solve_second(self, input_name : str) -> int:
        pass

    def load_input(self, input_name : str) -> List[str]:
        loaded_input = []
        with InputLoader(input_name) as input:
            for line in input:
                loaded_input.append(line)

        return loaded_input