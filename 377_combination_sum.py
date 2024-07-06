from typing import List

'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 
'''


class Solution_:
    def combinationSum4_backtrack(self, nums: List[int], target: int) -> int:
        def backtrack(remain, combo, start):
            if remain == 0:
                # Make a deep copy of the current combination.
                result.append(list(combo))
                return
            elif remain < 0:
                # Exceeded the sum with the current combination.
                return

            for i in range(start, len(nums)):
                # Add the number into the combination
                combo.append(nums[i])
                # Give the current number another chance, since we can use the same number unlimited times
                backtrack(remain - nums[i], combo, i)
                # Backtrack, remove the number from the combination
                combo.pop()

        result = []
        nums.sort()  # Sorting is optional.
        backtrack(target, [], 0)
        return len(result)

    def combinationSum4_memoization(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < nums[0]:
                return 0

            count = 0
            for num in nums:
                if n - num < 0:
                    break
                count += helper(n - num)

            memo[n] = count
            return count

        return helper(target)

    '''
    When you're calculating the combinations that sum up to a target using dynamic programming in the "Combination Sum IV" scenario, and you find that numbers like 1, 2, and 3 "make the cut" for a given target \(i=4\), this means each of these numbers can potentially contribute to a valid sum combination that equals 4. The significance of the subtraction results (3, 2, 1) from \(i=4\) when subtracted by numbers (1, 2, 3) is crucial and can be explained as follows:

    ### Subtraction Results Explained

    When you subtract a number `num` from the target `i` and get a non-negative result, that result (let's call it `remainder`) indicates:

    1. **Valid Combination Base**: The `remainder` shows how much you need to sum to after choosing `num` to reach the target `i`. This is the base for further combinations.
    2. **Building Upon Previous Solutions**: The subtraction result tells you to look back at the dynamic programming array `dp` at the position `remainder`. The value at `dp[remainder]` tells you how many ways there are to make up that remainder using the numbers in `nums`.
    3. **Linking to the Current Target**: By adding `dp[remainder]` to `dp[i]`, you effectively count all combinations that use `num` as part of the sum that makes `i`.

    ### Significance of Specific Subtraction Results for \(i = 4\)

    - **\(4 - 1 = 3\)**: This indicates that if you use `num = 1` in a combination to reach 4, you then need to find the number of ways to reach the remaining sum of 3 using any numbers from `nums`. The number of such ways is recorded in `dp[3]`.

    - **\(4 - 2 = 2\)**: Similarly, if you use `num = 2`, you then look for how many ways there are to reach the remaining sum of 2, as stored in `dp[2]`.

    - **\(4 - 3 = 1\)**: Using `num = 3` means checking how many ways to sum up to 1 using the numbers in `nums`, recorded in `dp[1]`.

    ### Accumulation in Dynamic Programming Array

    For `i = 4`, the dynamic programming update formula becomes:
    \[ dp[4] = dp[3] + dp[2] + dp[1] \]
    Each component of this sum directly relates to the subtraction results:
    - `dp[3]` (number of ways to reach 3 when 1 is used to reach 4)
    - `dp[2]` (number of ways to reach 2 when 2 is used to reach 4)
    - `dp[1]` (number of ways to reach 1 when 3 is used to reach 4)

    ### Conclusion

    This method of using subtraction results effectively harnesses previously computed values to build the solution for higher targets incrementally. Each step builds on the foundation of previous calculations, allowing the efficient computation of the number of combinations without redundant recalculations. It illustrates a fundamental principle of dynamic programming: solving complex problems by breaking them down into simpler subproblems and using the solutions of the subproblems to construct an answer to the problem.
    '''


class Solution:
    def combinationSum4_dp(self, nums: List[int], target: int) -> int:
        # Create an array dp with target + 1 slots, each initialized to zero.
        dp = [0] * (target + 1)
        # Set the base case: there is one way to reach the target sum of zero - using zero itself.
        dp[0] = 1

        # Iterate from 1 up to target
        for i in range(1, target + 1):
            # For each i, aim to fill dp[i] with the number of combinations that sum up to that value.
            for num in nums:
                print(f'num: {num}')
                # If i - num is a valid index (i.e., i - num >= 0), add dp[i - num] to dp[i].
                print(f'i-num: {i} - {num} = {i - num}')
                if i - num >= 0:
                    print(f'dp[i-num]: {dp[i-num]}')
                    dp[i] += dp[i - num]

        # dp[target] will hold the total number of combinations that make up the target sum.
        return dp[target]


if __name__ == "__main__":
    '''
    Input: nums = [1,2,3], target = 4
    Output: 7
    Explanation:
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    '''
    nums = [1, 2, 3]
    target = 4
    solution = Solution()
    result = solution.combinationSum4_dp(nums, target)
    assert result == 7, f"Expected output: 7, but returned: {result}"