from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        required = len(need)
        window = {}
        formed = 0
        left = 0
        ans_len = float("inf")
        ans_left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans_left = left

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

        if ans_len == float("inf"):
            return ""

        return s[ans_left : ans_left + ans_len]