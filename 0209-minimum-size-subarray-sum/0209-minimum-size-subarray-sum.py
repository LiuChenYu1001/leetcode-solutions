class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        ans = float("inf")

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                ans = min(ans, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return ans if ans != float("inf") else 0