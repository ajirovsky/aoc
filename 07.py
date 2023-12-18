from common.solver import Solver, pretty_print
from typing import List, Dict
import numpy as np
from functools import cmp_to_key


class DaySeven(Solver):
    
    def __parse_input(self, input : List[List[str]]) -> List[Dict]:
        return [{"cards": [card for card in line.split(" ")[0]], 
                 "bet" : int(line.split(" ")[1])} for line in input]
    
    def __evaluate_hand(self, hand : Dict) -> Dict:
        sorted_cards = sorted(hand["cards"])
        def cmp_card(l, r):
            if l["count"] != r["count"]:
                return l["count"] - r["count"]
            return self.card_order[l["card"]] - self.card_order[r["card"]]
        
        histogram = []
        existing_cards = np.unique(sorted_cards)
        for card in existing_cards:
            count = np.count_nonzero(np.array(sorted_cards) == card)
            histogram.append({"count": count, "card" : card})

        histogram.sort(key=cmp_to_key(cmp_card))
        values = [str(histogram[-1]["count"])]

        if len(histogram) > 1 and histogram[-2]["count"] == 2 and histogram[-1]["count"] < 4:
            values.append(str(histogram[-2]["count"]))
        
        hand["values"] = values
    
        return hand    
   
    def __evaluate_hand_sec(self, hand : Dict) -> Dict:
        sorted_cards = sorted(hand["cards"])
        def cmp_card(l, r):
            if l["count"] != r["count"]:
                return l["count"] - r["count"]
            return self.card_order[l["card"]] - self.card_order[r["card"]]
        
        histogram = []
        existing_cards = np.unique(sorted_cards)
        for card in existing_cards:
            mask = np.array(sorted_cards) == card
            count = np.count_nonzero(mask)
            histogram.append({"count": count, "card" : card})

        histogram.sort(key=cmp_to_key(cmp_card))
    
        for i in range(len(histogram)-1,-1 , -1):
            
            if histogram[i]["card"] != "J":
                histogram[i]["count"] += np.count_nonzero(np.array(sorted_cards) == "J")
                histogram = [h for h in histogram if h["card"] != "J"]
                break
        histogram.sort(key=cmp_to_key(cmp_card)) 
        
        histogram[-1]["count"] = min(histogram[-1]["count"], 5)
        
        values = [str(histogram[-1]["count"])]
        
        if len(histogram) > 1 and histogram[-2]["count"] >= 2 and histogram[-1]["count"] < 4:
            val = str(histogram[-2]["count"])
            values.append(val)
        
            
        hand["values"] = values
        
        
        return hand    
    
    @pretty_print
    def solve_first(self, input_name : str) -> int:
        CARD_TABLE = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        HAND_TABLE = ["5", "4", "32", "3", "22", "2",  "1", "0"]
        self.card_order = {k:v for k,v in zip(CARD_TABLE, range(len(CARD_TABLE), 0, -1))}
        self.hand_order = {k:v for k,v in zip(HAND_TABLE, range(len(HAND_TABLE), 0, -1))}

        def cmp_hands(l, r):
            l_key = self.hand_order["".join(l["values"])]
            r_key = self.hand_order["".join(r["values"])]
            
            if l_key != r_key:
                return l_key - r_key
            
            for val_i in range(min(len(l["cards"]), len(r["cards"]))):
                if l["cards"][val_i] != r["cards"][val_i]:
                    return self.card_order[l["cards"][val_i]] - self.card_order[r["cards"][val_i]]
                
        loaded_input = self.load_input(input_name)
        parsed = self.__parse_input(loaded_input)
        evaluated_hands = [self.__evaluate_hand(hand) for hand in parsed]
        
        evaluated_hands.sort(key=cmp_to_key(cmp_hands))
        
        val = [hand["bet"] * (i+1) for i,hand in enumerate(evaluated_hands)]
        return sum(val)
        
    
    @pretty_print
    def solve_second(self, input_name : str) -> int:
        CARD_TABLE = ["A", "K", "Q",  "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
        HAND_TABLE = ["5", "4", "32", "3", "22", "2",  "1", "0"]
        self.card_order = {k:v for k,v in zip(CARD_TABLE, range(len(CARD_TABLE), 0, -1))}
        self.hand_order = {k:v for k,v in zip(HAND_TABLE, range(len(HAND_TABLE), 0, -1))}
        
        def cmp_hands(l, r):
            l_key = self.hand_order["".join(l["values"])]
            r_key = self.hand_order["".join(r["values"])]
            
            if l_key != r_key:
                return l_key - r_key
            
            for val_i in range(min(len(l["cards"]), len(r["cards"]))):
                if l["cards"][val_i] != r["cards"][val_i]:
                    return self.card_order[l["cards"][val_i]] - self.card_order[r["cards"][val_i]]
                
        loaded_input = self.load_input(input_name)
        parsed = self.__parse_input(loaded_input)
        evaluated_hands = [self.__evaluate_hand_sec(hand) for hand in parsed]
        
        evaluated_hands.sort(key=cmp_to_key(cmp_hands))
        
        val = [hand["bet"] * (i+1) for i,hand in enumerate(evaluated_hands)]
        return sum(val)


if __name__ == "__main__":
    DaySeven().solve_first("07_small")
    DaySeven().solve_first("07")
    

    DaySeven().solve_second("07_small")
    DaySeven().solve_second("07")
