class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                h = nums[stack.pop()]

                if not stack:
                    left = 0
                else:
                    left = stack[-1] + 1

                right = i - 1

                if left <= k <= right:
                    ans = max(ans, h * (right - left + 1))

            stack.append(i)

        while stack:
            h = nums[stack.pop()]

            if not stack:
                left = 0
            else:
                left = stack[-1] + 1

            right = n - 1

            if left <= k <= right:
                ans = max(ans, h * (right - left + 1))

        return ans