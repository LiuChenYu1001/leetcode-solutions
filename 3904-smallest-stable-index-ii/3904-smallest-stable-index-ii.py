class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        left = 0
        for j in range(n):
            left = max(left, nums[j])

            if left - right[j] <= k:
                return j

        return -1