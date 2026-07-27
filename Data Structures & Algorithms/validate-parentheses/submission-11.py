class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        test = { '}': '{', ']': '[', ')': '(' }
        stack = []
        for ch in s:
            if ch in ['{','[','(']:
                stack.append(ch)
            elif stack and ch in [']','}',')']:
                if test[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
                
        return len(stack) == 0   
                