class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed conversion
            elif current_sum < target:
                left += 1   # Make the sum larger by moving rightward
            else:
                right -= 1  # Make the sum smaller by moving leftward
