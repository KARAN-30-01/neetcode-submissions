class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zers=0
        prod=1
        ans= [0]*len(nums)

        for i in nums:
            if not i:
                zers+=1

        if zers>1:
            return ans

        if zers==1:
            zindx=0
            for j,i in enumerate(nums):
                if i:
                    prod*=i
                if i==0:
                    zindx=j  
            ans[zindx] = prod          
            return ans

        for i in nums:
            prod*=i

        for j,i in enumerate(nums):
            ans[j] = prod//i
        return ans    


