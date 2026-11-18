from collections import defaultdict

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        count = defaultdict(int)
        n = len(nums)

        for num in nums:
            for integer in num:
                count[integer] += 1

        ans = [integer for integer, c in count.items() if c == n]
        ans.sort()

        return ans