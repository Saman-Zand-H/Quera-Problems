import numpy as np
from typing import List


default_board = (
    """8,0,0,0,0,0,0,0,0
       0,0,3,6,0,0,0,0,0
       0,7,0,0,9,0,2,0,0
       0,5,0,0,0,7,0,0,0
       0,0,0,0,4,5,7,0,0
       0,0,0,1,0,0,0,3,0
       0,0,1,0,0,0,0,6,8
       0,0,8,5,0,0,0,1,0
       0,9,0,0,0,0,4,0,0"""
       .replace("\r", "")
       .replace(" ", "")
       .split("\n")
)
default_board = [
    [int(i) for i in line.split(",")]
    for line in default_board
]


class Sudoku:
    def __init__(self, table: List[int|str]=default_board):
        self.table = np.array(table)
    
    @classmethod
    def create_subgrids(cls, arr: List[int|str]):
        if isinstance(arr, list):
            arr = np.array(arr)
        subgrids = []
        for i in range(0, 9, 3):
            subgrid = []
            for j in range(0, 9, 3):
                subgrid.append(
                    arr[j:j+3, i:i+3]
                )
            subgrids.append(subgrid)
        return np.array(subgrids)
    
    @classmethod
    def is_valid(cls, table: List[List[int]]):
        if isinstance(table, list):
            table = np.array(table)
        for row in range(len(table)):
            # check if we have duplicate in the row
            if len(set(table[row])) != len(table[row]):
                return False
            
        cols = table.swapaxes(1, 0)
        for col in range(len(cols)):
            if len(set(table[col])) != len(table[col]):
                return False
        
        subgrids = cls.create_subgrids(table)
        for col in subgrids:
            for row in col:
                if len(np.unique(row.flatten())) != len(row.flatten()):
                    return False
        
        return True    
        
        
if __name__ == "__main__":
    sample_complete = [
        [8, 2, 7, 1, 5, 4, 3, 9, 6], 
        [9, 6, 5, 3, 2, 7, 1, 4, 8], 
        [3, 4, 1, 6, 8, 9, 7, 5, 2], 
        [5, 9, 3, 4, 6, 8, 2, 7, 1],
        [4, 7, 2, 5, 1, 3, 6, 8, 9], 
        [6, 1, 8, 9, 7, 2, 4, 3, 5], 
        [7, 8, 6, 2, 3, 5, 9, 1, 4], 
        [1, 5, 4, 7, 9, 6, 8, 2, 3], 
        [2, 3, 9, 8, 4, 1, 5, 6, 7]
    ]
    print(Sudoku.is_valid(sample_complete))
        
