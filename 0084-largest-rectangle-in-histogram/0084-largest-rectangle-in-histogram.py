class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        ans = 0
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                ans = max(ans, h * w)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]

            if not stack:
                w = n
            else:
                w = n - stack[-1] - 1

            ans = max(ans, h * w)

        return ans