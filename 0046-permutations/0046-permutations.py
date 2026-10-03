class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                backtrack(path)
                path.pop()

        ans = []
        backtrack([])

        return ans