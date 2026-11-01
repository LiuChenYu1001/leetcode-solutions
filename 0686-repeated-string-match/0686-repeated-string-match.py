class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        count = (n + m - 1) // m
        s = a * (count + 1)

        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and b[i] != b[j]:
                j = lps[j - 1]

            if b[i] == b[j]:
                j += 1
                lps[i] = j

        j = 0
        for i in range(len(s)):
            while j > 0 and s[i] != b[j]:
                j = lps[j - 1]

            if s[i] == b[j]:
                j += 1

            if j == n:
                start = i - n + 1
                
                return (start + n + m - 1) // m

        return -1