class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                ans = max(ans, w * h)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]

            if not stack:
                w = n
            else:
                w = n - stack[-1] - 1

            ans = max(ans, w * h)

        return ans