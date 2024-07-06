'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''
from typing import List

'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.
'''


# Define the Solution class
class Solution:
    # Define the lengthOfLIS method that takes in a list of integers (nums) and returns an integer
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if nums is of len 0 or 1
        if len(nums) == 0:
            return 0
        elif(len(nums)) == 1:
            return 1

        # Initialize a list dp with length equal to the length of nums, where each element is initially set to 1
        dp = [1 for x in range(len(nums))]
        # Initialize a variable hi to keep track of the highest length of the increasing subsequence found so far
        hi = 1
        # Iterate through the elements of nums starting from the second element
        for i in range(1, len(nums)):
            # Iterate through the elements before the current element
            for j in range(i):
                # Get the value of the j-th element
                curr_j = nums[j]
                # If the current element is greater than the j-th element
                if nums[i] > nums[j]:
                    # Update the current dp element with the maximum value between its current value and dp[j] + 1
                    dp[i] = max(dp[i], dp[j] + 1)

            # If the current dp element is greater than the highest length found so far
            if dp[i] > hi:
                # Update the highest length
                hi = dp[i]

        # Return the highest length of the increasing subsequence
        return hi

# write driver here
if __name__ == "__main__":
    # Create an instance of the Solution class
    s = Solution()
    # Check if the lengthOfLIS method returns the expected result
    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4, f'Error: {s.lengthOfLIS([10,9,2,5,3,7,101,18])}'
