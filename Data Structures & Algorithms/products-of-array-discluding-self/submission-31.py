class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1]*n
        left_prod, right_prod = 1, 1
        
        for i in range(n):
            # Update the forward position with prefix product
            res[i] *= left_prod
            left_prod *= nums[i]
            
            # Update the backward position with suffix product
            res[n - 1 - i] *= right_prod
            right_prod *= nums[n - 1 - i]
            
        return res
