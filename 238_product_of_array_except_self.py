'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = [1] * len(nums)
        rightProd = [1] * len(nums)
        results = [1] * len(nums)

        for i in range(1, len(nums)):
            curr_left = leftProd[i - 1]
            curr_num = nums[i - 1]
            leftProd[i] = curr_left * curr_num
        
        for i in range(n-2, -1, -1):
            curr_right = rightProd[i + 1]
            curr_num = nums[i + 1]
            rightProd[i] = curr_right * curr_num
        
        for i in range(n):
            leftFactor = leftProd[i]
            rightFactor = rightProd[i]
            results[i] = leftFactor * rightFactor
        
        return results
    
# Example usage
if __name__=="__main__":
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums)) # [24,12,8,6]
    nums = [-1,1,0,-3,3]
    print(Solution().productExceptSelf(nums)) # [0,0,9,0,0]
