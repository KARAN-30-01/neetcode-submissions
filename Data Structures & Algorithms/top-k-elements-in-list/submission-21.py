class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequencies of each number -> O(N)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        # Step 2: Create buckets where the array index = frequency -> O(N)
        # The max possible frequency of any element is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 3: Iterate from the highest frequency bucket backwards -> O(N)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
