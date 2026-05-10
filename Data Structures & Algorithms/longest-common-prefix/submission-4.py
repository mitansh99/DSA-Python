class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in strs:
            if len(i) < len(prefix):
                prefix = i
        for i in range(1, len(strs)):
            for j in range(len(prefix)):
            #     if len(strs[i]) == 0: return ""
            #     if j+1 > len(strs[i]):
            #         break
                if prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break
        return prefix