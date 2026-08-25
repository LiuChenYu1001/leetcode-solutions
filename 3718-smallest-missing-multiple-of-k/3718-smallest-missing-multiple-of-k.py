class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        tem = k

        while True:
            if tem not in nums_set:
                return tem
            
            tem += k