from common.solver import Solver, pretty_print, timer
from typing import List



class DayEight(Solver):
    def __init__(self) -> None:
        super().__init__()
        self.lookup_routes = {}

    def __parse_input(self, input):
        instructions = input[0]
        path_dict = {path.split("=")[0][:-1] : [dst.replace(" ","").replace(")", "").replace("(", "") for dst in path.split("=")[1].split(",")] for path in input[2:]}
        return instructions, path_dict
    
    def __apply_path(self, loc, breaking_condition, instructions, path_dict):        
        steps = 0
        for inst in instructions:
            routes = path_dict[loc]
            loc = routes[0] if inst == "L" else routes[1]
            steps += 1
            if breaking_condition(loc):
                return loc, steps
        
        return loc, steps
    
    def __lcm_of_list(self, numbers):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        result = 1
        for num in numbers:
            result = (result * num) // gcd(result, num)
        return result

    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        instructions, path_dict = self.__parse_input(loaded_input)
        cnt = 0
        loc = "AAA"
        while loc != "ZZZ":
            loc, steps = self.__apply_path(loc, lambda x: x[-1] == "ZZZ", instructions, path_dict)
            cnt += steps
        return cnt
        

    @pretty_print
    @timer
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        instructions, path_dict = self.__parse_input(loaded_input)
        
        locations = [loc for loc in path_dict.keys() if loc[-1] == "A"]
        path_len = []
        for loc in locations:
            cnt = 0
            while loc[-1] != "Z":
                loc, steps = self.__apply_path(loc, lambda x: x[-1] == "Z", instructions, path_dict)
                cnt += steps
            path_len.append(cnt)
            
        
        return self.__lcm_of_list(path_len) 



if __name__ == "__main__":
    DayEight().solve_first("08_small")
    DayEight().solve_first("08_small2")
    DayEight().solve_first("08")
    

    DayEight().solve_second("08_small3")
    DayEight().solve_second("08")

