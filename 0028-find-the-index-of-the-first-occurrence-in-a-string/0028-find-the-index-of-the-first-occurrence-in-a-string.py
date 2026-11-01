class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)

        if n == 0:
            return 0

        lps = [0] * n
        j = 0

        for i in range(1, n):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]

            if needle[i] == needle[j]:
                j += 1
                lps[i] = j

        j = 0

        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == n:
                return i - n + 1

        return -1