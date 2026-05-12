class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [item for sublist in matrix for item in sublist]
        res = False
        for i in range(len(flat_list)):
            if flat_list[i] == target:
                res = True
        return res