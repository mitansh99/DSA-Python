class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            found = False
            for j in range(i,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    stack.append(j - i)
                    found = True
                    break
            if not found:
                stack.append(0)
        return stack
