class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 0
        right = x // 2 + 1

        while left < right:
            mid = (left + right) // 2

            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid

        return left - 1