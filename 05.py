from common.solver import Solver, pretty_print
import numpy as np

class DayFive(Solver):

    def __parse_input(self, input):
        maps = []
        for i, line in enumerate(input):
            if line == "":
                continue
            if "seeds" in line:
                seeds = [int(seed) for seed in line.split(":")[1][1:].split(" ")]
            if "-to-" in line:
                submaps = []
                j = i+1
                while j < len(input) and input[j] != "":
                    map_line = [int(dst) for dst in input[j].split(" ")]
                    submaps.append(map_line)
                    j += 1
                maps.append(submaps)
        return seeds, maps

    def __convert(self, seed, maps):
        for convert_map in maps:
            for submap in convert_map:
                if submap[1] <= seed < (submap[1] + submap[2]):
                    seed = seed - submap[1] + submap[0]
                    break
        return seed

    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        seeds, maps = self.__parse_input(loaded_input)
        val = [self.__convert(seed, maps) for seed in seeds]
        return min(val)

    @pretty_print
    def solve_second(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        seeds, maps = self.__parse_input(loaded_input)
        i = 0
        values = []
        while i < len(seeds) - 1:
            values.append(min([self.__convert(seed, maps) for seed in range(seeds[i], seeds[i] + seeds[i + 1])]))
            i += 2

        return min(values)

if __name__ == "__main__":
    DayFive().solve_first("05_small")
    

    DayFive().solve_second("05_small")
    # DayFive().solve_second("05")