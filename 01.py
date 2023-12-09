from common.solver import Solver, pretty_print
from typing import List

class DayOne(Solver):
    
    def __filter_numbers(self, loaded_input : List[str]) -> List[int]:
        filtered = [[int(char) for char in line  if char.isnumeric()] for line in loaded_input]
        return [x[0] * 10 + x[-1] for x in filtered]
    
    def __convert_strnums(self, line : str) -> str:
        lookup_table = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5",
                         "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9",
                         "1" : "1","2" : "2","3" : "3","4" : "4","5" : "5",
                         "6" : "6","7" : "7", "8":"8", "9" : "9"}
        indices = {}
        for sign in lookup_table.keys():
            offset = 0
            to_parse = line
            while len(to_parse) > 0:
                index = to_parse.find(sign)
                if index == -1:
                    break
                indices[index + offset] = sign
                offset += index + len(sign)
                to_parse = to_parse[index + len(sign):]
        
        ordered_signs = [key for key in indices.keys()]
        ordered_signs.sort()
        return "".join([lookup_table[indices[k]] for k in ordered_signs])
    
    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        filtered = self.__filter_numbers(loaded_input)
        final_value = sum([x for x in filtered])
        return final_value
    
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        converted = [self.__convert_strnums(line) for line in loaded_input]
        filtered = self.__filter_numbers(converted)
        final_value = sum([x for x in filtered])
        return final_value

if __name__ == "__main__":
    DayOne().solve_first("01_small")
    DayOne().solve_first("01")

    DayOne().solve_second("01b_small")
    DayOne().solve_second("01")