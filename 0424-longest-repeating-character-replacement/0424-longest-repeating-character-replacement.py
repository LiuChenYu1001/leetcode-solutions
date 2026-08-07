from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        ans = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count,  count[s[right]])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans