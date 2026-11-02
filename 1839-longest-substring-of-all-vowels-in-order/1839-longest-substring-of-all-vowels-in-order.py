class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        count = 1
        left = ans = 0

        for right in range(1, n):
            if word[right] < word[right - 1]:
                count = 1
                left = right

            elif word[right] > word[right - 1]:
                count += 1

            if count == 5:
                ans = max(ans, right - left + 1)

        return ans