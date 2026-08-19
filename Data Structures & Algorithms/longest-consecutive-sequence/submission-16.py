class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Still using the exact same "Smart Start" logic
            if num - 1 not in num_set:
                current_num = num + 1
                
                # Directly look up the next numbers in the set
                while current_num in num_set:
                    current_num += 1
                
                # Math calculation replaces the streak counter variable
                longest_streak = max(longest_streak, current_num - num)
                
        return longest_streak
