class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()    
        ans = 1

        for ch in s:
            if ch in seen:
                ans += 1
                seen = set()

            seen.add(ch)

        return ans