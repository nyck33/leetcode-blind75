'''
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    # expanded version
    def lengthOfLongestSubstring(self, s: str) -> int:
        # This dictionary maps characters to their last seen position in the string.
        last_pos = {}
        
        # The 'left' index indicates the start of the current substring without repeating characters.
        left = 0
        
        # 'max_len' will hold the length of the longest substring without repeating characters found so far.
        max_len = 0
        
        # Enumerate over the string, getting both the index ('right') and the character ('char') at that index.
        for right, char in enumerate(s):
            # If 'char' has already been seen, 'left' may need to move forward.
            # Get the last seen position of 'char', or -1 if 'char' has not been seen.
            last_seen_position = last_pos.get(char, -1)
            # Calculate the potential new start position, which is one position after xu'last_seen_position'.
            new_start_position = last_seen_position + 1
            # The new 'left' is the maximum of its current position and 'new_start_position'.
            left = max(left, new_start_position)
            
            # Calculate the length of the current substring.
            current_length = right - left + 1
            # Update 'max_len' if the current substring is longer than any previously found substring.
            max_len = max(max_len, current_length)
            
            # Update the last seen position of 'char' to be the current index 'right'.
            last_pos[char] = right
            
        # Return the maximum length of substring found.
        return max_len


# write driver
if __name__=="__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb")) #3
    print(s.lengthOfLongestSubstring("bbbbb")) #1
    print(s.lengthOfLongestSubstring("pwwkew")) #3
    print(s.lengthOfLongestSubstring("")) #0
    print(s.lengthOfLongestSubstring(" ")) #1
    print(s.lengthOfLongestSubstring("a")) #1
    print(s.lengthOfLongestSubstring("ab")) #2
    print(s.lengthOfLongestSubstring("aab")) #2