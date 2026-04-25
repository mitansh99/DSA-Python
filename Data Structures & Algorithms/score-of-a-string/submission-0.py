class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i in range(0,len(s)):
            ctr = 0
            if i < len(s) - 1:
                ctr = ord(str(s[i+1])) - ord(str(s[i]))
                result += abs(ctr)
        return result
