class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            min_num = min(nums[i:])
            max_num = max(nums[:i + 1])
            score = max_num - min_num
            if score <= k:
                return i

        return -1