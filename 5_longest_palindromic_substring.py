class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        make grid, then fill diagonal then fill in the first after diagonal filled for len 2 palindromic substring? then fill in rest checking i+1, j-1 was the letter before the same?  Then if True, mark current True
        '''
        num_chars = len(s)
        
        grid = [[0 for x in range(num_chars)] for y in range(num_chars)]

        for i in range(num_chars):
            grid[i][i] = 1

        longest_start = 0 #init starting idex of longest palindrom found
        max_len = 1 # init max len of longest palindrome found

        # check for 2 char palindromes
        for i in range(num_chars - 1):
            if s[i] == s[i+1]:
                grid[i][i+1] = 1
                longest_start = i
                max_len = 2
        
        # check for palindromes longer than 2 chars
        for length in range(3, num_chars + 1):
            for i in range(num_chars - length+1):
                j = i + length - 1 # Determine the end index 'j' based on the length
                # check if first and last chars of current substring  are the same and if the substring nested inside it at i +1, j-1 (since i is start and j is end for current substring) was a palindrome 
                if s[i] == s[j] and grid[i+1][j-1]: 
                    grid[i][j] = 1 # is palindrome
                    if length > max_len:
                        max_len = length 
                        longest_start = i

        return s[longest_start: longest_start + max_len]


        