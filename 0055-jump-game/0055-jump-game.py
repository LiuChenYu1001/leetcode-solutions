class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: 
            return True
        
        far = 0
        n = len(nums)

        for i in range(n):
            if far < i:
                return False

            far = max(far, nums[i] + i)

            if far >= n-1:
                return True

        return True