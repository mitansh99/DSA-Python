class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] *len(temperatures)
        i = 0
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    stack[i] = j - i
                    break
            i += 1
        return stack
