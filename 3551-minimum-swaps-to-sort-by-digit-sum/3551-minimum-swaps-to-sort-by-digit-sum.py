class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sum_digit(nums):
            return sum(int(d) for d in str(nums))

        n = len(nums)
        sorted_nums = sorted(nums, key = lambda num: (sum_digit(num), num))
        pos = {num: i for i, num in enumerate(sorted_nums)}
        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue

            j = i
            circle = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                circle += 1

            ans += circle - 1

        return ans