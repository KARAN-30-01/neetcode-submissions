class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)

        # sorted_num_counter = sorted(num_counter.keys(), lambda x: Counter(x), reverse = True)
        sorted_nums = sorted(num_counter.keys(), key=lambda x: num_counter[x], reverse=True)

        return sorted_nums[:k]
        