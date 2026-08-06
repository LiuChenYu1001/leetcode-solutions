class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            ans = 1
            for ch in str(num):
                ans *= int(ch)
            
            return ans

        while True:
            if digit_product(n) % t == 0:
                return n
            else:
                n += 1
                continue 