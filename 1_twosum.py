'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # write code
        # Create a dictionary to store the indices of the elements
        indices = {}
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            # Check if the complement exists in the dictionary
            if complement in indices:
                # Return the indices of the current number and its complement
                return [indices[complement], i]
            # Add the current number and its index to the dictionary
            indices[num] = i
        # If no solution is found, return an empty list
        return []
    
if __name__ == "__main__":
    # Example usage
    # Input list of numbers
    nums = [2,7,11,15]
    target = 9
    # Create an instance of the class
    solution = Solution()
    # Call the function
    print(solution.twoSum(nums, target)) # Output: [0, 1]
    '''
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    '''
    nums = [3,2,4]
    target = 6
    print(solution.twoSum(nums, target)) # Output: [1, 2]
    '''
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
    '''
    nums = [3,3]
    target = 6
    print(solution.twoSum(nums, target)) # Output: [0, 1]
    '''
    Example 4:

    Input: nums = [3,2,3], target = 6
    Output: [0,2]
    '''
    nums = [3,2,3]
    target = 6
    print(solution.twoSum(nums, target)) # Output: [0, 2]
    '''
    Example 5:

    Input: nums = [1,3,4,2], target = 6
    Output: [2,3]
    '''
    nums = [1,3,4,2]
    target = 6
    print(solution.twoSum(nums, target)) # Output: [2, 3]
    '''
    Example 6:

    Input: nums = [1,3,4,2], target = 7
    Output: [2,3]
    '''
    nums = [1,3,4,2]
    target = 7
    print(solution.twoSum(nums, target)) # Output: [2, 3]
    '''
    Example 7:

    Input: nums = [1,3,4,2], target = 5
    Output: [1,2]
    '''
    nums = [1,3,4,2]
    target = 5
    print(solution.twoSum(nums, target)) # Output: [1, 2]
    