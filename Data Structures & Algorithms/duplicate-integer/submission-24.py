class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsData = set(nums)

        if (len(numsData) != len(nums)):
            return True
        else:
            return False
            