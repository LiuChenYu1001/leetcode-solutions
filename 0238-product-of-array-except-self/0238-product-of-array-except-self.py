class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        prefix = [1] 
        for i in range(1, n):
            prefix.append(prefix[-1] * nums[i-1]) 
            
        suffix = [1]
        for j in range(n-2, -1, -1): 
            suffix.append(suffix[-1] * nums[j+1])
        suffix.reverse()
        
        ans = [] 
        for k in range(n):
            ans.append(prefix[k] * suffix[k]) 
            
        return ans