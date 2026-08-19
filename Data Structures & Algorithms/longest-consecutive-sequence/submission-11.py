class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 1. Convert to a set for O(1) constant-time value lookups
        num_set = set(nums)
        longest_streak = 0
        
        # 2. Iterate through the unique numbers
        for num in num_set:
            # Check if 'num' is the ABSOLUTE START of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Build the streak exactly like your loop logic did
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Keep track of the maximum streak found so far
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
