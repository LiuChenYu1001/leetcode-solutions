class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((num, i) for i, num in enumerate(nums))
        ans = [0] * n
        left = 0

        while left < n:
            right = left + 1

            while right < n and arr[right][0] - arr[right - 1][0] <= limit:
                right += 1

            indices = sorted(arr[i][1] for i in range(left, right))

            for k, index in enumerate(indices):
                ans[index] = arr[left + k][0]

            left = right

        return ans