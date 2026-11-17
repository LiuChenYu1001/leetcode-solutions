class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        ans = even = odd = 0

        for num in arr:
            if num % 2 == 0:
                even += 1
            else:
                odd, even = even + 1, odd

            ans = (ans + odd) % MOD

        return ans