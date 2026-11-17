class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float("inf")
        n = len(nums)

        for i in range(n - l + 1):
            j = l

            for j in range(l, r + 1):
                total = sum(nums[i:i + j])

                if total > 0:
                    ans = min(ans, total)

        return ans if ans != float("inf") else -1