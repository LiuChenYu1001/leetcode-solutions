class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = right

        def need_parts(cap):
            parts = 1
            cur = 0
            for n in nums:
                if cur + n > cap:
                    parts += 1
                    cur = 0
                cur += n
            return parts

        while left <= right:
            mid = (left + right) // 2

            if need_parts(mid) <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans