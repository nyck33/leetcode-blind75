'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''
# Time Complexity :  O(n)
# Space Complexity : O(1)
import collections
# This class implements the solution to the problem
class Solution(object):
    '''
    def characterReplacement(self, s, k):
        # Initialize variables
        maxlen, largestCount = 0, 0
        arr = collections.Counter()  # Counter to keep track of character counts
        print(f'arr: {arr}')
        
        # Iterate through the string
        for idx in range(len(s)):
            arr[s[idx]] += 1  # Increment the count of the current character
            largestCount = max(largestCount, arr[s[idx]])  # Update the largest count
            
            # Check if the number of replacements needed is greater than k
            if maxlen - largestCount >= k:
                arr[s[idx - maxlen]] -= 1  # Decrement the count of the character at the start of the window
            else:
                maxlen += 1  # Increment the length of the window
        
        return maxlen  # Return the length of the longest substring
    '''

    def characterReplacement(self, s: str, k: int) -> int:
        # 1. Initialize the left pointer of the sliding window
        l = 0

        # 2. Initialize a dictionary to store the frequency of each character
        c_frequency = {}

        # 3. Initialize a variable to store the length of the longest valid substring
        longest_str_len = 0

        # 4. Iterate over the string with the right pointer of the sliding window
        for r in range(len(s)):
            # 5. Update the frequency count of the current character
            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1

            # 6. Calculate the number of replacements needed to replace all characters in the current window
            cells_count = r - l + 1 # + 1 for zero indexing
            # cells count is window size, then subtract the most frequent character count from the window size and check if it is less than or equal to k, the number of replacements allowed
            if cells_count - max(c_frequency.values()) <= k:
                # 7. If the number of replacements needed is less than or equal to k, update the length of the longest valid substring
                longest_str_len = max(longest_str_len, cells_count)
            else:
                # 8. If the number of replacements needed is more than k, move the left pointer of the window to the right and update the frequency count
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    c_frequency.pop(s[l])
                l += 1

        # 9. Return the length of the longest valid substring
        return longest_str_len
    
if __name__=="__main__":
    s = "ABAB"
    k = 2
    sol = Solution()
    print(sol.characterReplacement(s, k))
    assert sol.characterReplacement(s, k) == 4

    #Output: 4
    #Explanation: Replace the two 'A's with two 'B's or vice versa.

    s = "AABABBA" 
    k = 1
    print(sol.characterReplacement(s, k))
    assert sol.characterReplacement(s, k) == 4


    #Output: 4
