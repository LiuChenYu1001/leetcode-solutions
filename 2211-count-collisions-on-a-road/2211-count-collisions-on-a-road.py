class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        ans = 0

        for direction in directions:
            if direction == "R":
                stack.append(direction)

            elif direction == "S":
                while stack and stack[-1] == "R":
                    stack.pop()
                    ans += 1

                stack.append("S")

            elif direction == "L":
                if stack:
                    if stack[-1] == "R":
                        stack.pop()
                        ans += 2

                        while stack and stack[-1] == "R":
                            stack.pop()
                            ans += 1
                    else:
                        ans += 1

                    stack.append("S")

        return ans