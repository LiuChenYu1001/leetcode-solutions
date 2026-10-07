class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for ch in s:
            if ch == "(":
                stack.append(score)
                score = 0
            else:
                inner_score = max(1, 2 * score)
                score = inner_score + stack.pop()

        return score