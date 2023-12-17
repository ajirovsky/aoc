from common.solver import Solver, pretty_print
from typing import List, Union
import numpy as np

class DayFive(Solver):

    def __parse_first(self, input : List[List[str]]) -> Union[List[int], List[int]]:
        times = [int(t) for t in input[0].split(":")[1].split(" ") if t.isnumeric()]
        distances = [int(d) for d in input[1].split(":")[1].split(" ") if d.isnumeric()]
        return times, distances
    
    def __parse_second(self, input : List[List[str]]) -> Union[int, int]:
        times = [t for t in input[0].split(":")[1].split(" ") if t.isnumeric()]
        distances = [d for d in input[1].split(":")[1].split(" ") if d.isnumeric()]
        
        return int("".join(times)), int("".join(distances))
    
    def __solve_race(self, time : int, record : int):
        return len([s*(time-s) for s in range(time) if s*(time-s) > record])
    
    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        times, distances = self.__parse_first(loaded_input)
        val = [self.__solve_race(t,d) for t,d in zip(times,distances)]
        return np.prod(val)
    
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        times, distances = self.__parse_second(loaded_input)
        return self.__solve_race(times,distances)
        



if __name__ == "__main__":
    DayFive().solve_first("06_small")
    DayFive().solve_first("06")
    

    DayFive().solve_second("06_small")
    DayFive().solve_second("06")
    