class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = []
        product = 1
        zero_count = 0

        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                product = product * i

        for i in nums:

            if zero_count > 1:
                prod.append(0)

            elif zero_count == 1:

                if i == 0:
                    prod.append(product)
                else:
                    prod.append(0)

            else:
                prod.append(product // i)

        return prod