'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
'''

# write a recursive algo for the above problem
# The idea is to find the pivot element in the rotated sorted array. The pivot element is the minimum element in the array.
# The pivot element is the only element in the array which is smaller than its previous element. If there is no previous element, then there is no rotation (the first element is the smallest). We can do this by modifying the binary search algorithm.
# The binary search is used to find the index of the pivot element. The pivot element divides the array into two parts. The left part is greater than the pivot element and the right part is less than the pivot element.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Call the binary_search function with initial parameters
        return self.binary_search(nums, 0, len(nums) - 1)
    
    def binary_search(self, nums: List[int], left: int, right: int) -> int:
        # Base case: If the array is not rotated
        if nums[left] <= nums[right]:
            return nums[left]
        
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the middle element is greater than the next element
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        
        # If the middle element is smaller than the previous element
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        # If the right half is sorted, search in the left half
        if nums[mid] < nums[right]:
            return self.binary_search(nums, left, mid - 1)
        # If the left half is sorted, search in the right half
        return self.binary_search(nums, mid + 1, right)
    
'''
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
'''
    
if __name__ == "__main__":
    nums = [3,4,5,1,2]
    # Create an instance of the class
    solution = Solution()
    # Call the function
    print(solution.findMin(nums)) # Output: 1

    # reuse the instance of the class
    nums = [4,5,6,7,0,1,2]
    # Call the function
    print(solution.findMin(nums)) # Output: 0

    nums = [11,13,15,17]
    # Call the function
    print(solution.findMin(nums)) # Output: 11

    