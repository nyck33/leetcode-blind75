'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize variables to keep track of the maximum and minimum product since min can become max if next number is negative
        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        
        # Iterate through the array
        for i in range(1, len(nums)):
            # If the current number is negative, swap the maximum and minimum product because the product of two negative numbers is positive
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Update the maximum and minimum product
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
            
            # Update the overall result
            result = max(result, max_product)
        
        return result
