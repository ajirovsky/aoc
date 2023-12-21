from common.solver import Solver, pretty_print
from typing import List
import numpy as np

class DayEleven(Solver):
    
    def __create_gravitized(self, input : List[List[str]]) -> List[List[str]]:
        extended = np.copy(input)
        
        for i in range(extended.shape[0] - 1, -1, -1):
            if np.count_nonzero(input[i] == "#") == 0:
                extended = np.insert(extended, i, np.full(input[i].shape, "."), axis=0)
        
        for i in range(input.shape[1] - 1, -1, -1):
            if np.count_nonzero(input.T[i] == "#") == 0:
                extended = np.insert(extended, i, np.full(extended.shape[0], "."), axis=1)

        return extended
    
    def __create_gravity_mask(self, input : List[List[str]]) -> List[List[int]]:
        mask = np.zeros(input.shape)
        
        for i in range(mask.shape[0] - 1, -1, -1):
            if np.count_nonzero(input[i] == "#") == 0:
                mask[i] = np.ones(input[i].shape)

        for i in range(mask.shape[0] - 1, -1, -1):
            if np.count_nonzero(input.T[i] == "#") == 0:
                mask[:, i] = np.ones(input.T[i].shape)
        return mask

    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        loaded_input = np.array([[a for a in line] for line in loaded_input])
        gravitized_input = self.__create_gravitized(loaded_input)
        
        galaxies = np.argwhere(gravitized_input == "#")
        paths = [sum(abs(g1-g2)) for i, g1 in enumerate(galaxies) for g2 in galaxies[i+1:]]

        return sum(paths)        
            
            
            
    def __get_distance(self, g_from : List[int], g_to : List[int], gravity_mask : List[List[int]]) -> int:
        dist = 0
        a, b = np.copy(g_from), np.copy(g_to)
        
        
        while a[0] != b[0]:
            a[0] += 1 if a[0] < b[0] else -1
            dist += 1 if gravity_mask[*a] == 0 else 1_000_000 
            
        while a[1] != b[1]:
            a[1] += 1 if a[1] < b[1] else -1
            dist += 1 if gravity_mask[*a] == 0 else 1_000_000 
        
        return dist
        
    
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        loaded_input = np.array([[a for a in line] for line in loaded_input])
        gravity_mask = self.__create_gravity_mask(loaded_input)
        galaxies = np.argwhere(loaded_input == "#")
        # paths = [self.__get_distance(g1, g2, gravity_mask) for i, g1 in enumerate(galaxies) for g2 in galaxies[i+1:]]
        paths = []
        for i, g1 in enumerate(galaxies):
            for g2 in galaxies[i+1:]:
                paths.append(self.__get_distance(g1, g2, gravity_mask))
            
        return sum(paths)
        

if __name__ == "__main__":
    DayEleven().solve_first("11_small")
    DayEleven().solve_first("11")

    DayEleven().solve_second("11_small")
    DayEleven().solve_second("11")
    
