from common.solver import Solver, pretty_print
from typing import List
import numpy as np

class DayNine(Solver):
    
    def __solve_line(self, val : List[int]) -> int:
        processed_arr = [val]
        while len(np.unique(processed_arr[-1])) != 1:
            processed_arr.append([processed_arr[-1][i] - processed_arr[-1][i-1] for i in range(1, len(processed_arr[-1]))])
        for i in range(len(processed_arr) - 2, -1, -1):
            processed_arr[i].append(processed_arr[i][-1] + processed_arr[i+1][-1])
        return processed_arr[0][-1]
        
    def __solve_line_sec(self, val : List[int]) -> int:
        processed_arr = [val]
        while len(np.unique(processed_arr[-1])) != 1:
            processed_arr.append([processed_arr[-1][i] - processed_arr[-1][i-1] for i in range(1, len(processed_arr[-1]))])
        for i in range(len(processed_arr) - 2, -1, -1):
            processed_arr[i] = [processed_arr[i][0] - processed_arr[i+1][0]] + processed_arr[i]
        return processed_arr[0][0]
    
    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        val = [self.__solve_line([int(num) for num in line.split(" ")]) for line in loaded_input]
        return np.sum(val)
    
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        val = [self.__solve_line_sec([int(num) for num in line.split(" ")]) for line in loaded_input]
        return np.sum(val)
        

if __name__ == "__main__":
    DayNine().solve_first("09_small")
    DayNine().solve_first("09")
    

    DayNine().solve_second("09_small")
    DayNine().solve_second("09")
