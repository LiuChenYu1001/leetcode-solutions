class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        cur = ""

        for ch in s:
            if ch == "(":
                stack.append(cur)
                cur = ""
            elif ch == ")":
                cur = stack.pop() + cur[::-1]
            else:
                cur += ch

        return cur