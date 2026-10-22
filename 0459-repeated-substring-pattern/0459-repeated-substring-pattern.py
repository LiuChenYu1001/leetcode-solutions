class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        lps = [0] * n
        j = 0

        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]

            if s[i] == s[j]:
                j += 1
                lps[i] = j

        length = n - lps[-1]

        return lps[-1] > 0 and n % length == 0