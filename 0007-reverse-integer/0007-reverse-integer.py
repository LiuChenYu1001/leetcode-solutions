class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        ans = 0

        while x:
            if x < 0:
                digit = -(abs(x) % 10)
                x = -(-x // 10)

            else:
                digit = x % 10
                x //= 10

            if ans * 10 + digit > INT_MAX:
                return 0
            if ans * 10 + digit < INT_MIN:
                return 0

            ans = ans * 10 + digit

        return ans