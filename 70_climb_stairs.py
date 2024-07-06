'''
70. Climbing Stairs
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

'''
#Walk me through this problem like a white board coding test and explain the time complexity of your solution.  Write your response in the first person so I can read it for the interviewer sitting in front of me.  Try to use point form rather than paragraphs.  I will ask you questions if I need more information.  I will also ask you to write code for this problem.


class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0 for x in range(n + 1)]
        # base cases
        ways[0] = 1
        ways[1] = 1

        for i in range(2, n + 1):
            way = ways[i-1] + ways[i-2]
            ways[i] = way
        
        return ways[n]

if __name__ == "__main__":
    n = 2
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 2, f"Expected output: 2, but returned: {result}"

    n = 3
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 3, f"Expected output: 3, but returned: {result}"
    
    n = 4
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 5, f"Expected output: 5, but returned: {result}"
    
    n = 5
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 8, f"Expected output: 8, but returned: {result}"
    
    n = 6
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 13, f"Expected output: 13, but returned: {result}"
    
    n = 7
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 21, f"Expected output: 21, but returned: {result}"
    
    n = 8
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 34, f"Expected output: 34, but returned: {result}"
    
    n = 9
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 55, f"Expected output: 55, but returned: {result}"
    
    n = 10
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 89, f"Expected output: 89, but returned: {result}"
    
    n = 11
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 144, f"Expected output: 144, but returned: {result}"
    
    n = 12
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == 233, f"Expected output: 233, but returned: {result}"
    
   