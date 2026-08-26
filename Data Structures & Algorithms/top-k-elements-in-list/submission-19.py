class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 0
            dict1[i] += 1
        
        # 1. Correctly sort descending (highest frequency first)
        dict2 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        
        # 2. Cleanly slice the first k keys
        return list(dict2.keys())[:k]
