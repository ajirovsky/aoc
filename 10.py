from common.solver import Solver, pretty_print
from collections import deque
from typing import List, Union
import numpy as np
import math
from functools import cmp_to_key

class DayTen(Solver):
    def __init__(self) -> None:
        super().__init__()

        self.connectivity_table = {"|" : { "|" : [[1,0], [-1, 0]], "L" : [[1, 0]], "J" : [[1, 0]], "F": [[-1, 0]], "7" : [[-1, 0]], "S" : [[1,0], [-1, 0]]},
                                   "-" : {"L" : [[0, -1]], "J" : [[0, 1]], "F" : [[0, -1]], "7" : [[0, 1]], "-" : [[0, 1], [0, -1]], "S" : [[0, 1], [0, -1]]},
                                   "L" : {"|" : [[-1, 0]], "J" : [[0, 1]], "F" : [[-1, 0]], "7" : [[-1, 0], [0, 1]], "-" : [[0, 1]], "S" : [[-1, 0], [0, 1]]},
                                   "J" : {"|" : [[-1, 0]], "L" : [[0, -1]], "F" : [[-1, 0], [0, -1]], "7" : [[-1, 0]], "-" : [[0, -1]], "S" : [[-1, 0], [0, -1]]},
                                   "7" : {"|" : [[1, 0]], "L" : [[1,0], [0, -1]], "J" : [[1,0]], "F" : [[0, -1]], "-" : [[0, -1]], "S" : [[1, 0], [0, -1]]},
                                   "F" : {"|" : [[1,0]], "L" : [[1,0]], "J" : [[1, 0], [0, 1]], "7" : [[0, 1]], "-" : [[0,1]], "S" : [[1, 0], [0,1]]},
                                   "S" : {"|" : [[1,0], [-1, 0]], "-" : [[0, 1], [0, -1]], "L" : [[1,0], [0, -1]], "J" : [[1, 0], [0, 1]], "7" : [[-1, 0], [0, 1]], 
                                          "F" : [[-1, 0], [0, -1]]}
        }
        self.route_table = {"L" : [[-1, 0],[0, 1]], "J" : [[-1, 0], [0, -1]], "7" : [[0, -1], [0, 1]], "F" : [[1,0], [0,1]]}
        
    def __check_neighbours(self, idx : List[int], arr : List[List[str]]) -> List[Union[int,int]]:
        key_val = arr[*idx]
        possible_routes = self.connectivity_table[key_val]

        valid_steps = [idx+n for n in [[0,1], [0,-1], [1,0], [-1,0]] if 0 <= (idx+n)[0] < len(arr) and 0 <= (idx+n)[1] < len(arr[0]) and arr[*(idx+n)] in possible_routes and n in possible_routes[arr[*(idx+n)]]]
        return valid_steps

    @pretty_print
    def solve_first(self, input_name : str) -> int:
        loaded_input = self.load_input(input_name)
        loaded_input = np.array([[c for c in line] for line in loaded_input])
        
        starting_pos = np.argwhere(loaded_input == "S")[0]
        q = deque()

        pos_key = "-".join([str(a) for a in starting_pos])
        visited = {}


        q.append((starting_pos, 0))
        while len(q) > 0:
            pos, cnt = q.popleft()
            pos_key = "-".join([str(a) for a in pos])
            
            if pos_key in visited:
                continue
                    
            found = [(f, cnt + 1) for f in self.__check_neighbours(pos, loaded_input)]

            visited[pos_key] = cnt
            q += found

        return max([cnt for cnt in visited.values()])    
    
    def __point_in_polygon(self, x, y, polygon):  #stolen from chatgpt
        n = len(polygon)
        inside = False

        for i in range(n):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % n]

            # Check if the point is on the edge of the polygon
            if (y1 == y2 and y == y1 and min(x1, x2) <= x <= max(x1, x2)) or \
            (x1 == x2 and x == x1 and min(y1, y2) <= y <= max(y1, y2)):
                return True

            # Check for intersection with the ray
            if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
                inside = not inside

        return inside
    
    
    
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        
        loaded_input = self.load_input(input_name)
        loaded_input = np.array([[c for c in line] for line in loaded_input])
        
        starting_pos = np.argwhere(loaded_input == "S")[0]
        q = deque()

        pos_key = "-".join([str(a) for a in starting_pos])
        visited = []


        q.append(starting_pos)
        edge_points = []
        while len(q) > 0:
            pos = q.popleft()
            pos_key = "-".join([str(a) for a in pos])
            
            if pos_key in visited:
                continue

            
            found = self.__check_neighbours(pos, loaded_input)
            uncoded = [int(a) for a in pos_key.split("-")]

            edge_points.append(uncoded)    
            visited.append(pos_key)
            
            for f in found:
                q.appendleft(f)

        

        mask = np.zeros(loaded_input.shape)

        for idx in edge_points:
            mask[*idx] = 1
            if loaded_input[*idx] == "S":
                mask[*idx] = 2
        
        cnt = 0
        for idx, _ in np.ndenumerate(loaded_input):
            if list(idx) in edge_points:
                continue
            cnt += self.__point_in_polygon(*idx, edge_points)
            if self.__point_in_polygon(*idx, edge_points):
               mask[*idx] = 4

        return cnt

        

if __name__ == "__main__":
    DayTen().solve_first("10_small")
    DayTen().solve_first("10")

    
    

    DayTen().solve_second("10_small3")
    DayTen().solve_second("10")
