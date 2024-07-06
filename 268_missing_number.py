'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        xor_sum = 0
        # XOR all indices from 0 to n
        for i in range(n + 1):
            # print binary of xor_sum and i
            print(f"i: {bin(i)}, xor_sum: {bin(xor_sum)}")
            xor_sum ^= i
            print(f"xor_sum: {bin(xor_sum)}")
        # XOR all elements in the array
        for i in range(n):
            print(f"num: {bin(nums[i])}, xor_sum: {bin(xor_sum)}")
            xor_sum ^= nums[i]
            print(f"xor_sum: {bin(xor_sum)}")
        return xor_sum

# write driver
if __name__=="__main__":

    nums = [3, 0, 1]  # Example input
    solution = Solution()
    result = solution.missingNumber(nums)
    assert result == 2, f"Expected output: 2, but returned: {result}"

    nums = [0, 1]  # Example input
    solution = Solution()
    result = solution.missingNumber(nums)
    assert result == 2, f"Expected output: 2, but returned: {result}"

    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]  # Example input
    solution = Solution()
    result = solution.missingNumber(nums)
    assert result == 8, f"Expected output: 8, but returned: {result}"

    nums = [0]  # Example input
    solution = Solution()
    result = solution.missingNumber(nums)
    assert result == 1, f"Expected output: 1, but returned: {result}"

    nums = [1]  # Example input
    solution = Solution()
    result = solution.missingNumber(nums)
    assert result == 0, f"Expected output: 0, but returned: {result}"