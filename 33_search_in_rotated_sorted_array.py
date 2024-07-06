from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initializing left and right pointers
        left, right = 0, len(nums) - 1
        
        # Loop until left pointer is less than or equal to right pointer
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If the middle element is equal to the target
            if nums[mid] == target:
                # Return the index of the middle element
                return mid
            
            # If the left element is less than or equal to the middle element
            if nums[left] <= nums[mid]:
                # If the target is within the range of left and middle elements
                if nums[left] <= target <= nums[mid]:
                    # Update the right pointer to search in the left half
                    right = mid - 1
                else:
                    # Update the left pointer to search in the right half
                    left = mid + 1
            else:
                # If the right element is less than the middle element
                # This means that the rotation has mixed up the sorted order
                # and the right half of the array is not sorted in ascending order
                
                # If the target is within the range of middle and right elements
                if nums[mid] <= target <= nums[right]:
                    # Update the left pointer to search in the right half
                    left = mid + 1
                else:
                    # Update the right pointer to search in the left half
                    right = mid - 1
                    # Update the left pointer to search in the right half
                    left = mid + 1
        
        # Return -1 if the target is not found
        return -1
    

    

if __name__ == "__main__":
    # Example usage
    # Input list of numbers
    nums = [4,5,6,7,0,1,2]
    target = 0
    # Create an instance of the class
    solution = Solution()
    # Call the function
    print(solution.search(nums, target)) # Output: 4
    '''
    Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
    Example 3:

    Input: nums = [1], target = 0
    Output: -1
    '''

    # Example usage
    # Input list of numbers
    nums = [4,5,6,7,0,1,2]
    target = 3

    # Create an instance of the class
    solution = Solution()

    # Call the function
    print(solution.search(nums, target)) # Output: -1

    # Example usage
    nums = [1]
    target = 0
    print(solution.search(nums, target)) # Output: -1