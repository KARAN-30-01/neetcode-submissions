class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        col_num = len(matrix[0])
        row_num = len(matrix)
        
        # Standard inclusive boundaries
        start = 0
        end = (col_num * row_num) - 1
        
        while start <= end:
            curr_idx = (start + end) // 2
            
            # Map 1D index to 2D matrix positions
            row_idx = curr_idx // col_num
            col_idx = curr_idx % col_num
            
            curr_val = matrix[row_idx][col_idx]
            
            if curr_val == target:
                return True
            elif target < curr_val:
                end = curr_idx - 1     # Narrow search to the left half
            else:
                start = curr_idx + 1    # Narrow search to the right half
                
        return False
