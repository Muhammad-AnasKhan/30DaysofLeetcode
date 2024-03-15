class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        format(n, 'b'): Converts the integer n to a binary string.

        .zfill(32): Pads the binary string with zeros on the left to reach a length of 32.
        
        [::-1]: Reverses the bit order of the binary string.
        
        int(..., 2): Converts the reversed binary string back to an integer (base 2).
        '''
        return int(format(n, 'b').zfill(32)[::-1], 2)
        