'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

'''
Intuition
The goal is to find the minimum window in string s that contains all characters from string t. The intuition is to use a sliding window approach with two pointers.

Approach
Initialize a character array map of size 128 to store the frequency of characters in string t.
Initialize variables count, start, end, minLen, and startIndex.
Iterate through each character in string t and update the character frequency in the map.
Use two pointers (start and end) to slide the window and find the minimum window that contains all characters from string t.
Increment end and decrease the frequency in map for each character encountered until all characters from t are present in the window.
When all characters from t are present, update minLen and startIndex based on the current window size and starting index.
Increment start and increase the frequency in map until the window no longer contains all characters from t.
After the iteration, the minimum window is found, and the result is a substring of s starting from startIndex with length minLen.
Complexity
Time complexity: O(n), where n is the length of string s.
Space complexity: O(1), as the map array has a constant size (128).
'''
import pandas as pd
from typing import List, Dict, Tuple

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_dict = {}
        n = len(s)
        t_arr = list(t)
        len_t = len(t_arr)

        incl_letters_d = {}
        # check this dict each time make key 
        for i in range(len_t):
            curr = t_arr[i]
            if curr not in incl_letters_d:
                incl_letters_d[curr] = 1
            else:
                incl_letters_d[curr] += 1
        
        segment_d = {}

        # iterate from min of num chars in the must include str and len of the search space string
        j= 0
        for i in range(len_t-1, n+1):
            curr_substr = s[j:i] 
        pass

    def minWindow_sol(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Initialize a character array map of size 128 to store the frequency of characters in string t.
        map = [0] * 128
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0

        # Iterate through each character in string t and update the character frequency in the map. ASCII integer
        for char in t:
            map[ord(char)] += 1

        # Use two pointers (start and end) to slide the window and find the minimum window that contains all characters from string t.
        # iterate s from end=0 to len(s)
        while end < len(s):
            # if curr letter of s in map of t, decrement count of t as we found one
            s_end = s[end]
            print(f's_end: {s_end}')
            
            if map[ord(s[end])] > 0:
                count -= 1
            # decrement the map for the letter in s
            map[ord(s[end])] -= 1
            # increment end
            end += 1

            # When all characters from t are present in substring, update minLen and startIndex based on the current window size and starting index.
            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start # was able to find all chars where end ended up in s

                s_start = s[start]
                print(f's_start: {s_start}')

                if map[ord(s[start])] == 0:
                    count += 1
                map[ord(s[start])] += 1
                start += 1

        # After the iteration, the minimum window is found, and the result is a substring of s starting from startIndex with length minLen.
        return "" if min_len == float('inf') else s[start_index:start_index + min_len]

    def minWindow_sol_debug(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Initialize a dictionary to store the frequency of characters in string t.
        map = {chr(i): 0 for i in range(128)}
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0

        # Iterate through each character in string t and update the character frequency in the map.
        for char in t:
            map[char] += 1

        # Use two pointers (start and end) to slide the window and find the minimum window that contains all characters from string t.
        while end < len(s):
            # if curr letter of s in map of t, decrement count of t as we found one
            s_end = s[end]
            print(f's_end: {s_end}')

            if map[s_end] > 0:
                count -= 1
            # decrement the map for the letter in s
            map[s_end] -= 1
            # increment end
            end += 1

            # When all characters from t are present in substring, update minLen and startIndex based on the current window size and starting index.
            while count == 0: # found all the letters in t
                if end - start < min_len: # beats the min len
                    start_index = start # set this as start of the window
                    min_len = end - start #

                s_start = s[start]
                print(f's_start: {s_start}')

                # window is shrunk when start incremented so whatever letter is at map[s_start] is incremented
                # because one more character from t needs to be found again to form a valid window
                if map[s[start]] == 0:
                    count += 1
                map[s[start]] += 1 # increment as star will be incremented so the letter in t has to be found again
                start += 1

        # After the iteration, the minimum window is found, and the result is a substring of s starting from startIndex with length minLen.
        return "" if min_len == float('inf') else s[start_index:start_index + min_len]




if __name__=="__main__":
    '''
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    Example 2:

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
    Example 3:

    Input: s = "a", t = "aa"
    Output: ""
    '''
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    # print the solution and then assert
    ans = sol.minWindow_sol_debug(s, t)
    print(f'ans: {ans}')
    assert ans == "BANC", f'Error: {ans}'

    