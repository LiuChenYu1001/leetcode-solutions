class Solution:
    def minInsertions(self, s: str) -> int:
        left = right = 0

        for ch in s:
            if ch == "(":
                right += 2

                if right == 1:
                    left += 1
                    right -= 1

            else:
                right -= 1

                if right < 0:
                    left += 1
                    right = 1

        return left + right    