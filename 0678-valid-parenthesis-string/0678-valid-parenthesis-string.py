class Solution:
    def checkValidString(self, s: str) -> bool:
        open_can = 0
        for ch in s:
            if ch == ')':
                open_can -= 1
            else:
                open_can += 1
            if open_can < 0:
                return False

        close_can = 0
        for ch in reversed(s):
            if ch == '(':
                close_can -= 1
            else:
                close_can += 1
            if close_can < 0:
                return False

        return True