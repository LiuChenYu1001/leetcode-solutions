class Solution:
    def minEnd(self, n: int, x: int) -> int:
        remain = n - 1
        ans = x
        bit = 0

        while remain:
            if (x >> bit) & 1 == 0:
                if remain & 1:
                    ans |= 1 << bit
                remain >>= 1

            bit += 1
        
        return ans