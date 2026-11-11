class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                bottom = stack.pop()

                if not stack:
                    break

                left = stack[-1]
                width = i - left - 1
                ans += (min(height[left], height[i]) - height[bottom]) * width

            stack.append(i)

        return ans