class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, path):
            ans.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        nums.sort()
        ans = []
        backtrack(0, [])

        return ans