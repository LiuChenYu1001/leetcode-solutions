class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: abs(x))
        left, right = 0, len(nums) - 1
        score = 0

        while left <= right:
            score += nums[right] ** 2
            right -= 1

            if left <= right:
                score -= nums[left] ** 2
                left += 1

        return score