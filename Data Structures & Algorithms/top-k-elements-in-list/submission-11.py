class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i] = 0
            dict1[i]+=1    
        dict2 = dict(sorted(dict1.items(), key=lambda item: item[1]), reverse=True)
        return list(dict2.keys())[len(dict2)-1-k:len(dict2)-1]