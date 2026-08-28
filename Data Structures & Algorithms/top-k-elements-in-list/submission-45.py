from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies in O(N) time
        count = Counter(nums) 
        
        # 2. Extract top k frequent elements in O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)
