class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = decrease = 1
        ans = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increase += 1
                decrease = 1
            elif nums[i] < nums[i - 1]:
                decrease += 1
                increase = 1
            else:
                increase = decrease = 1

            ans = max(ans, increase, decrease)

        return ans