class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        steps = 0
        cur_end = 0
        next_end = 0

        for i in range(n):
            next_end = max(next_end, i + nums[i])

            if next_end >= n - 1:
                return steps + 1

            if i == cur_end:
                steps += 1
                cur_end = next_end

        return steps