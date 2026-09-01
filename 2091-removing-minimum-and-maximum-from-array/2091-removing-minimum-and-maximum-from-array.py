class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        max_num = min_num = nums[0]
        max_idx = min_idx = 0

        for i in range(1, n):
            if nums[i] > max_num:
                max_num = nums[i]
                max_idx = i

            if nums[i] < min_num:
                min_num = nums[i]
                min_idx = i

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        return min(right + 1, n - left, left + 1 + n - right)