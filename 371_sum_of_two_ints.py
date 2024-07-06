class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max, in decimal form is 2147483647
        MAX = 0x7FFFFFFF # = 0111 1111 1111 1111 1111 1111 1111 1111, 
        # 32 bits integer min, in decimal form is -2147483648, This is because, in two's complement representation, the decimal value of a binary number with a leading 1 is calculated by flipping all the bits, adding 1 to the result, and then negating it. If you flip all the bits of 80000000, you get 7FFFFFFF, which is 2147483647 in decimal. Adding 1 to this gives 2147483648, and negating it gives -2147483648.
        MIN = 0x80000000 # = 1000 0000 0000 0000 0000 0000 0000 0000, 
        # mask to get last 32 bits
        mask = 0xFFFFFFFF # = 1111 1111 1111 1111 1111 1111 1111 1111

        while b != 0:
            # calculate sum without carrying
            a_xor_b = a ^ b
            print(f"a_xor_b: {a_xor_b}")
            a_after_mask = a_xor_b & mask
            print(f"a_after_mask: {a_after_mask}")
            a_and_b = (a & b)
            print(f"a_and_b: {a_and_b}")
            a_b_after_left_shift = (a_and_b << 1)
            print(f"a_b_after_left_shift: {a_b_after_left_shift}")
            b_after_lshift_and_mask = a_b_after_left_shift & mask
            print(f"b_after_lshift_and_mask: {b_after_lshift_and_mask}")
            # After these two operations, a contains the sum of the original a and b without any carry, and b contains the carry. The loop continues with these new values of a and b, effectively adding the carry to the sum in each iteration, until there is no carry left (i.e., until b becomes 0). At this point, a contains the final sum of the original a and b.
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # if a is greater than max, get a's two's complement
        return a if a <= MAX else ~(a ^ mask)

# Example usage
solution = Solution()
print(solution.getSum(5, 3))  # Output: 8
