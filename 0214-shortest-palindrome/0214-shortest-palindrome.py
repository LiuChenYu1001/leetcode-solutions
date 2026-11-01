class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        pattern = s + "#" + rev
        n = len(pattern)
        j = 0
        lps = [0] * n

        for i in range(1, n):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]

            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        longest = lps[-1]

        return rev[:len(s) - longest] + s