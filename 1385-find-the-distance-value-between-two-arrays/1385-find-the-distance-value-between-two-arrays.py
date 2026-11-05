import bisect
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for num in arr1:
            i = bisect.bisect_left(arr2, num)

            ok = True

            if i < len(arr2) and abs(arr2[i] - num) <= d:
                ok = False
            if i-1 >= 0 and abs(num - arr2[i-1]) <= d:
                ok = False
            
            if ok:
                ans += 1

        return ans