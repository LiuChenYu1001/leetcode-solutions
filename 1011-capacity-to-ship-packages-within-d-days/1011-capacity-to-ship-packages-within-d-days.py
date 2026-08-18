class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = right

        def need(cap):
            d = 1
            cur = 0

            for w in weights:
                if cur + w > cap:
                    d += 1
                    cur = 0

                cur += w

            return d

        while left <= right:
            mid = (left + right) // 2

            if need(mid) <= days:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans