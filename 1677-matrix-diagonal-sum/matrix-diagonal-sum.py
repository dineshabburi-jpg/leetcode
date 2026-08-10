class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        for i in range(n):
            # Add primary diagonal element
            total_sum += mat[i][i]
            
            # Add secondary diagonal element
            total_sum += mat[i][n - 1 - i]
            
        # If n is odd, the center element was added twice, so subtract it once
        if n % 2 != 0:
            total_sum -= mat[n // 2][n // 2]
            
        return total_sum