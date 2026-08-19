class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        ans = right

        def hours_needed(k):
            total = 0
            for p in piles:
                total += (p + k - 1) // k
            return total

        while left <= right:
            mid = (left + right) // 2

            if hours_needed(mid) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans