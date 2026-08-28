class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # With division: If you have 2 or more zeros, then everything will be 0 no matter what
        # If 1 zero: Every number is zero, except ith position with zero is the product of all numbers
        # If no zeros: Divide the product by nums[i]

        product = 1
        res = []
        zeros = 0

        for num in nums:
            if num:
                product *= num
            else:
                zeros += 1 # determine product without the zero

        if zeros > 1:
            return [0] * len(nums) # if more than one zero, product list garuanteed to be all zeros

        for num in nums:
            if zeros: # if there is 1 zero, every position is 0 except position with 0 is the product of other nums
                res.append(product) if num == 0 else res.append(0)
            else: # no zeros, then each position is product // num
                res.append(product//num)

        return res