class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(1, n, 2):
            if s[i - 1:i + 1] == "10" or s[i - 1:i + 1] == "01":
                ans += 1

        return ans