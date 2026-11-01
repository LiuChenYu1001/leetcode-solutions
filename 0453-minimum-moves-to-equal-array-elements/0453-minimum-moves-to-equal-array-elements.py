class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        ans = 0

        for num in nums:
            ans += num - min_num

        return ans