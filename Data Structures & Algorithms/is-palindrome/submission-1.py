class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join([x for x in s if x.isalnum()])
        a = strs.lower()
        return a == a[::-1]