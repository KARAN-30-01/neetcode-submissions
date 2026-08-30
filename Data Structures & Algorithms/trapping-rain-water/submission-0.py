class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        area = 0

        while i < len(height) - 1:

            j = i + 1

            # Find first wall >= left wall
            while j < len(height) and height[j] < height[i]:
                j += 1

            # If none exists, use tallest wall on the right
            if j == len(height):
                j = i + 1

                for k in range(i + 1, len(height)):
                    if height[k] >= height[j]:
                        j = k

            water_height = min(height[i], height[j])

            for k in range(i + 1, j):
                area += water_height - height[k]

            i = j

        return area