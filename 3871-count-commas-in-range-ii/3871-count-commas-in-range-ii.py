class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        tem = 1000

        while n >= tem:
            ans += (n - tem + 1)
            tem *= 1000

        return ans