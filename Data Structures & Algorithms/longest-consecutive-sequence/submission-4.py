class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num1 = sorted(set(nums)) 
        a=1 
        b=[] 
        for idx,i in enumerate(num1):
            
            if idx> 0:
                if num1[idx] == num1[idx-1]+1:
                    a+=1
                else:
                    b.append(a)
                    a=1    
        
        b.append(a)
        
        if not nums:
            return 0

        return max(b)            


            
             
            



        