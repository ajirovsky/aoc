from common.solver import Solver, pretty_print
import numpy as np

class DayTwo(Solver):
    def __init__(self):
        self.limits = {"red":12, "green" : 13, "blue" : 14}
    
    def __parsed_line(self, line : str) -> int:
        limits = self.limits
        id = int(line.split(":")[0].split(" ")[1])
        values = [{color.split(" ")[2] : int(color.split(" ")[1]) for color in values.split(",")} 
            for values in "".join(line.split(":")[1:]).split(";") ]
        maxed= {k : max([val[k] for val in values if k in val]) for k in limits.keys()}

        return id if all([maxed[k] <= limits[k] for k in limits.keys()]) else 0
    
    def __parsed_line_second(self, line : str) -> int:
        limits = self.limits
        values = [{color.split(" ")[2] : int(color.split(" ")[1]) for color in values.split(",")} 
            for values in "".join(line.split(":")[1:]).split(";") ]
        maxed= {k : max([val[k] for val in values if k in val]) for k in limits.keys()}
        return np.prod([val for val in maxed.values()])
    
    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        parsed_games = [self.__parsed_line(line) for line in loaded_input]
        return sum(parsed_games)
        
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        parsed_games = [self.__parsed_line_second(line) for line in loaded_input]
        return sum(parsed_games)
    

if __name__ == "__main__":
    DayTwo().solve_first("02_small")
    DayTwo().solve_first("02")

    DayTwo().solve_second("02_small")
    DayTwo().solve_second("02")