class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        if n == 2:
            return -1

        min_s = min(s)
        max_s = max(s)

        if min_s == s[0] or max_s == s[-1]:
            return 1

        if min_s in s[1:-1] or max_s in s[1:-1]:
            return 2

        return 3