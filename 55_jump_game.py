'''
ou are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''
from typing import List
class Solution:
    def canJump_dp(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        # Iterate through each index in the array
        for i in range(n):
            if dp[i]:
                # Iterate through each possible jump length from the current index
                for j in range(1, nums[i] + 1):
                    if i + j < n: # cannot reach the end but...
                        dp[i + j] = True # can reqch this index
                    # If we can reach the last index, return True
                    if i + j >= n - 1:
                        return True
        # If we cannot reach the last index, return False
        return dp[-1]
    
    # This function checks if it is possible to reach the last index of the given array by jumping through the elements
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reachable = 0
        
        # Iterate through each index in the array
        for i in range(n):
            # If the current index is greater than the maximum reachable index, cannot reach this index from the previous indices given max jump lens at previous positions
            if i > max_reachable:
                return False
            
            # Update the maximum reachable index based on the current index and its jump length
            max_reachable = max(max_reachable, i + nums[i])
            
            # If the maximum reachable index is greater than or equal to the last index, it means we can reach the last index
            if max_reachable >= n - 1:
                return True
        
        # If we cannot reach the last index, return False
        return False
    
if __name__=="__main__":
    nums = [2,3,1,1,4]
    solution = Solution()
    result = solution.canJump_dp(nums)
    assert result == True, f"Expected output: True, but returned: {result}"

    nums = [3,2,1,0,4]
    solution = Solution()
    result = solution.canJump_dp(nums)
    assert result == False, f"Expected output: False, but returned: {result}"