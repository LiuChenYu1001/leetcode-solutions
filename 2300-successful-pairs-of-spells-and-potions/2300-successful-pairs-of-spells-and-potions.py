import bisect

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        n = len(potions)
        check = []

        for i in range(n):
            check.append((potions[i] + success - 1) // potions[i])

        ans = []
        check.sort()

        for spell in spells:
            idx = bisect.bisect_right(check, spell)
            ans.append(idx)

        return ans