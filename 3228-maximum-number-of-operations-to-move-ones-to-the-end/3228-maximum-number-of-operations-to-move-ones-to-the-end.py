class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        one = 0

        for i, c in enumerate(s):
            if c == "1":
                one += 1

            elif i == len(s) - 1 or s[i + 1] == "1":
                ans += one

        return ans