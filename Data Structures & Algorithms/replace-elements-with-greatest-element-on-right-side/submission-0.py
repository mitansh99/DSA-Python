class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            if i == len(arr) - 1 :
                result.append(-1)  
            else: 
                maxForCurrent = max(arr[i+1:len(arr)])
                result.append(maxForCurrent)
        return result
