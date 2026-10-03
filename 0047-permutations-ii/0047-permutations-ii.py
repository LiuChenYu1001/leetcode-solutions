class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if used[i] == True:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:  #遇到相同數字時，前一個還沒用，就不能先用後一個
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        used = [False] * len(nums)
        ans = []
        nums.sort()
        backtrack([])

        return ans