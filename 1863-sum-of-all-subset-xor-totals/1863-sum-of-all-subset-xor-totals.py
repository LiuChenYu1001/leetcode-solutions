class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(idx, xor):
            if idx == n:
                return xor

            not_take = dfs(idx + 1, xor)
            take = dfs(idx + 1, xor ^ nums[idx])

            return not_take + take

        return dfs(0, 0)