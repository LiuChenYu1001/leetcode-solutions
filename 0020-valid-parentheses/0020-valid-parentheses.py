class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in match:
                if not stack:
                    return False

                top = stack.pop()
                if match[ch] != top:
                    return False

            else:
                stack.append(ch)

        return not stack