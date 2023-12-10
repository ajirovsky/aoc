from common.solver import Solver, pretty_print
import numpy as np

class DayFour(Solver):

    def __parse_card(self, line):
        card_num = line.split(":")[0].split(" ")[-1]
        numbers = line.split(":")[1].split("|")
        winning_numbers = [num for num in numbers[0][1:].split(" ") if num.isnumeric()]
        card_numbers = [num for num in numbers[1][1:].split(" ") if num.isnumeric()]
        return card_num, [winning_numbers, card_numbers]
    
    def __calculate_winnings(self, values):

        winning_numbers = values[0]
        card_numbers = values[1]
        card_winning_numbers = [val for val in card_numbers if val in winning_numbers]
        return card_winning_numbers
        
    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        parsed = [self.__parse_card(line)[1] for line in loaded_input]
        calculated = [self.__calculate_winnings(line) for line in parsed]
        calculated = [2**(len(game)-1) for game in calculated if len(game) > 0]
        return int(np.sum(calculated))
        
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        loaded_input = self.load_input(input_name)
        parsed = [self.__parse_card(line)[1] for line in loaded_input]
        calculated = [self.__calculate_winnings(line) for line in parsed]
        calculated = [len(line) for line in calculated]
        copies = [1] * len(calculated)

        for i in range(len(calculated)):
            for j in range(i+1, calculated[i]+i+1):
                copies[j] += copies[i]         
        
        return sum(copies)
    

if __name__ == "__main__":
    DayFour().solve_first("04_small")
    DayFour().solve_first("04")
    
    
    DayFour().solve_second("04_small")
    DayFour().solve_second("04")