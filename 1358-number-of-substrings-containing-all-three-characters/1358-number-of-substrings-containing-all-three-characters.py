from collections import Counter

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = Counter()
        ans = 0
        left = 0
        n = len(s)

        for right in range(n):
            count[s[right]] += 1

            while len(count) == 3:
                ans += n - right

                count[s[left]] -= 1

                if count[s[left]] == 0:
                    del count[s[left]]

                left += 1

        return ans