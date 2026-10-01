class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_digit(num):
            res = 0
            arr = list(str(num))

            for ar in arr:
                res += int(ar)
            
            return res

        for i, num in enumerate(nums):
            if i == sum_digit(num):
                return i

        return -1