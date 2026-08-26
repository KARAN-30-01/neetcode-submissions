from heapq import heapify, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        heap = [(-f, n) for n, f in count.items()]
        result = []
        heapify(heap)
        
        for _ in range(0, k):

            result.append(heappop(heap)[1])

        return result