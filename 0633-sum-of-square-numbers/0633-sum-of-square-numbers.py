class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)

        while left <= right:
            val = left * left + right * right

            if val == c:
                return True
            elif val < c:
                left += 1
            else:
                right -= 1

        return False