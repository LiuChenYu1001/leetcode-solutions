class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                cur = num
                length = 1

                while cur + 1 in nums_set:
                    cur += 1
                    length += 1

                ans = max(ans, length)

        return ans