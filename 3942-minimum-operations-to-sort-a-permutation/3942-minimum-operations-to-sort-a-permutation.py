class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        ans = float("inf")

        if all(nums[(zero + i) % n] == i for i in range(n)):
            ans = min(ans, zero, n - zero + 2)

        if all(nums[(zero - i) % n] == i for i in range(n)):
            ans = min(ans, zero + 2, n - zero)

        return ans if ans != float("inf") else -1