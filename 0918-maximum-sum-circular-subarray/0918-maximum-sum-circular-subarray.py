class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans_max = float("-inf")
        tem_max = 0
        ans_min = float("inf")
        tem_min = 0
        total = sum(nums)

        for num in nums:
            tem_max += num
            ans_max = max(ans_max, tem_max)

            if tem_max <= 0:
                tem_max = 0

            tem_min += num
            ans_min = min(ans_min, tem_min)

            if tem_min >= 0:
                tem_min = 0

        if ans_max < 0:
            return ans_max

        return max(ans_max, total - ans_min)