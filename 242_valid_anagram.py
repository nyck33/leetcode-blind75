'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict = {}
        n = len(s)
        t_arr = list(t)
        for i in range(n):
            if s[i] not in freq_dict:
                freq_dict[s[i]] = 1
            else:
                freq_dict[s[i]] += 1
        for i in range(n):
            if t_arr[i] in freq_dict:
                freq_dict[t_arr[i]] -= 1
            else:
                return False
        for key in freq_dict:
            if freq_dict[key] != 0:
                return False
        return True