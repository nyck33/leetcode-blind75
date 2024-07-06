from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Call the binary_search function with initial parameters
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        # Base case: If left index is greater than right index, target is not found
        if left > right:
            return -1

        # Calculate the middle index
        mid = (left + right) // 2

        # If the middle element is equal to the target, return the index
        if nums[mid] == target:
            return mid

        # Check if the left half of the array is sorted
        if nums[left] <= nums[mid]:
            # Check if the target is within the left half
            if nums[left] <= target <= nums[mid]:
                # Recursively search the left half
                return self.binary_search(nums, left, mid - 1, target)
            else:
                # Recursively search the right half
                return self.binary_search(nums, mid + 1, right, target)
        else:
            # Check if the target is within the right half
            if nums[mid] <= target <= nums[right]:
                # Recursively search the right half
                return self.binary_search(nums, mid + 1, right, target)
            else:
                # Recursively search the left half
                return self.binary_search(nums, left, mid - 1, target)

if __name__ == "__main__":
    # Create an instance of the Solution class
    s = Solution()

    # Define the input list and target value
    nums = [4,5,6,7,0,1,2]
    target = 0

    # Call the search method and print the result
    print(s.search(nums, target))  # Output: 4