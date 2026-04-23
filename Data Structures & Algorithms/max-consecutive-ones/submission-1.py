class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        local = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                local += 1
            else: 
                local = 0
            count = max(local, count)
        return count