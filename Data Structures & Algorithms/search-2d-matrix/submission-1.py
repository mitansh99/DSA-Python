class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return True if any(item == target for sublist in matrix for item in sublist) else False