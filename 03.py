import numpy as np
from common.solver import Solver, pretty_print
from typing import List, Set

def counter(f):
    counter = 1
    number_ended = False
    def func(x):
        nonlocal counter, number_ended
        if not f(x):
            if not number_ended:
                counter += 1
            number_ended = True
            return 0
        number_ended = False
        return counter
    return func

class DayThree(Solver):

    def __check_neighbourhood(self, numeric_mask : np.array, index : List) -> Set:
        neighbours = [[index[0] - 1, index[1]], [index[0] + 1, index[1]],
                      [index[0], index[1] - 1], [index[0], index[1] + 1],
                      [index[0] - 1, index[1] -1], [index[0] - 1 , index[1] + 1],
                      [index[0] + 1, index[1] -1], [index[0] + 1, index[1] + 1]]
        dims = numeric_mask.shape
        neighbours = [ x for x in neighbours if x[0] >= 0 and x[1] >= 0 and x[0] < dims[0] and x[1] < dims[1]]
    
        return {numeric_mask[*x] for x in neighbours if numeric_mask[*x] != 0}
        
    def __create_mask(self, input : List[List[int]], filter_func, generate_id=False) -> np.array:
        id_generate = counter(filter_func) if generate_id else (lambda x : 1 if filter_func(x) else 0)
        return np.array([[id_generate(x) for x in line] for line in input])
        
    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        converted = np.array([[x for x in line] for line in loaded_input])
        numeric_mask = self.__create_mask(converted, lambda x : x.isnumeric(), generate_id=True)
        symbolic_mask = self.__create_mask(converted, lambda x : x != "." and not x.isnumeric())
        found_numbers = set.union(*[self.__check_neighbourhood(numeric_mask, list(idx))for idx in np.argwhere(symbolic_mask == 1)])
        return sum([int("".join(converted[numeric_mask == num_id])) for num_id in found_numbers])
        
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        converted = np.array([[x for x in line] for line in loaded_input])
        numeric_mask = self.__create_mask(converted, lambda x : x.isnumeric(), generate_id=True)
        symbolic_mask = self.__create_mask(converted, lambda x : x == "*" and not x.isnumeric())
        found_numbers = [self.__check_neighbourhood(numeric_mask, list(idx)) for idx in np.argwhere(symbolic_mask == 1) 
                         if len(self.__check_neighbourhood(numeric_mask, list(idx))) == 2]
    
        return sum([np.prod([(int("".join(converted[numeric_mask == num_id]))) for num_id in gear_numbers]) for gear_numbers in found_numbers])
    
if __name__ == "__main__":
    DayThree().solve_first("03_small")
    DayThree().solve_first("03")

    DayThree().solve_second("03_small")
    DayThree().solve_second("03")
    