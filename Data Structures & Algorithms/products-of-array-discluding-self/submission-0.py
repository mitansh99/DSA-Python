class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result= []
        for i in range(len(nums)):
            cr = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    cr *= nums[j] 
            result.append(cr)
            
        return result