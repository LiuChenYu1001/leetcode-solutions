class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                pre_idx = stack.pop()
                ans[pre_idx] = i - pre_idx

            stack.append(i)

        return ans