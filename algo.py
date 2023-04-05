from collections import defaultdict
from typing import Tuple, DefaultDict, List


class ProcessArray():

    def __init__(self, max_val: int, input_array: List[int]):
        self.input_array = input_array
        self.max_val = max_val
        self.d_lower, self.d_higher = self.split_input_into_dicts(max_val)


    def split_input_into_dicts(self, max_val: int) -> Tuple[DefaultDict]:
        d_lower, d_higher = defaultdict(int), defaultdict(int)
        division = max_val // 2
        for i in input:
            if not isinstance(i, int) or i < 0:
                raise ValueError(f'Input values - {i} - should be natural numbers only')
            if i > max_val:
                raise ValueError(f'Input values cannot be higher than {max_val}')
            
            if i <= division:
                d_lower[i] += 1
            else:
                d_higher[i] += 1

        return d_lower, d_higher
    

    def create_pairs(self) -> List[Tuple[int]]:
        output = []
        for first_val, first_count in self.d_lower.items():
            second_val = self.max_val - first_val
            second_count = self.d_higher.get(second_val)
            if second_count:
                output.extend([(first_val, second_val)
                               for _ in range(min(first_count, second_count))])
        return output
    

if __name__ == '__main__':
    input = [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8 , 11, 12, 0]
    t = ProcessArray(12, input)
    print(t.create_pairs())