'''
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the variable to store the reversed bits
        result = 0  
        
        # Iterate 32 times to reverse all the bits
        for i in range(32):  
            # Shift the bits of the result to the left by 1 position, to make space for the next bit
            result <<= 1  

            print(f'i: {i}')
            print(f'n: {bin(n)}')
            print(f"result: {bin(result)}\n")
            
            # Set the rightmost bit of the result to the current bit of n
            #result |= n & 1
            #resultOrN = result | n
            #print(f"resultOrN: {bin(resultOrN)}")
            #resultOrNAnd1 = resultOrN & 1
            #print(f"resultOrNAnd1: {bin(resultOrNAnd1)}") 
            # n & 1 will give the rightmost bit of n since AND = 1 if n's last bit is 1, otherwise 0
            # then do an OR operation with the result to set the rightmost bit of the result to the current bit of n
            result = result | (n & 1) #0001
            #print(f"result: {bin(result)}")
            # Shift the bits of n to the right by 1 position so that the next bit becomes the rightmost bit
            print(f'n before: {bin(n)}')
            n >>= 1  
            print(f'n after: {bin(n)}')

        
        # Return the reversed bits as an integer
        return result  
    
# write driver based on comments at top
if __name__=="__main__":
    
    # n = 43261596  # Example input in decimal
    n = 0b00000010100101000001111010011100  # Example input
    solution = Solution()
    result = solution.reverseBits(n)
    assert result == 964176192, f"Expected output: 964176192, but returned: {result}"

    # second example
    n = 0b11111111111111111111111111111101
    solution = Solution()
    #result = solution.reverseBits(n)
    #assert result == 3221225471, f"Expected output: 3221225471, but returned: {result}"