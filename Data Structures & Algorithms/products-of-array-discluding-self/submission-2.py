class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc = nums.count(0)
        if zc > 1:
            return [0] * len(nums)
        if zc == 1:
            mul = 1
            for num in nums:
                if num != 0:
                    mul *= num
            idx = nums.index(0)
            ans = [0] * len(nums)
            ans[idx] = mul
            return ans
        mul = 1
        for num in nums:
            mul *= num

        return [mul // num for num in nums]