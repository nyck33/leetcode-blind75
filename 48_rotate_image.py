'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Can transpose and reverse or reverse and transpose
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    # print matrix after transpose
                    print(f'matrix after transpose\n: {self.print_matrix(matrix)}')

        def reverse_rows(matrix):
            for r in range(len(matrix)): # rows
                left, right = 0, len(matrix[0]) - 1
                while left < right: # cols
                    matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                    left += 1
                    right -= 1
                    # print matrix after reverse
                    print(f'matrix after reverse:\n {self.print_matrix(matrix)}')
        
        transpose(matrix)
        reverse_rows(matrix)

    def print_matrix(self, matrix):
        for row in matrix:
            print(row)
        
'''
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
sol.rotate(matrix)
print(f'rotated matrix: {matrix}') # [[7,4,1],[8,5,2],[9,6,3]]
assert matrix == [[7,4,1],[8,5,2],[9,6,3]], f'Error: {matrix}'

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol = Solution()
#sol.rotate(matrix)
#print(f'rotated matrix: {matrix}') # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
