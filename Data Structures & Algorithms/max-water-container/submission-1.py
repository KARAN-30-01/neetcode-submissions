class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j= len(heights)-1
        maxa=0

        while i<j:
            
            if (j-i)*(min ( heights[i] , heights[j] ))>maxa:
                maxa=(j-i)*(min ( heights[i] , heights[j] ))

            if heights[j] > heights[i]:
                i+=1  
                continue  
            else:
                j-=1 
                continue
            i+=1
            j-=1
        return maxa           

