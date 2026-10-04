class Solution:
    def checkValidString(self, s: str) -> bool:
        open_can = 0

        for ch in s:
            if ch == ")":
                open_can -= 1
            else:
                open_can += 1

            if open_can < 0:
                return False
        
        closed_can = 0
        for ch in reversed(s):
            if ch == "(":
                closed_can -= 1
            else:
                closed_can += 1
            
            if closed_can < 0:
                return False

        return True