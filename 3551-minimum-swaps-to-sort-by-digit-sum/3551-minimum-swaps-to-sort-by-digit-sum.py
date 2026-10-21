class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sum_digit(num):
            return sum(int(d) for d in str(num))

        n = len(nums)
        sorted_num = sorted(nums, key = lambda x: (sum_digit(x), x))
        pos = {num: idx for idx, num in enumerate(sorted_num)}
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