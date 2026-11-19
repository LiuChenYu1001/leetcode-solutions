class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        diff = []

        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i - 1])

        if len(nums) == 3:
            return 0

        low = 0
        high = sum(diff)

        high = min(
            high - diff[0] - diff[1],
            high - diff[-1] - diff[-2],
            high - diff[0] - diff[-1]
        )

        return low + high