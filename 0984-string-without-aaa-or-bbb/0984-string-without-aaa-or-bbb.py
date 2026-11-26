class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []

        while a > 0 or b > 0:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                if ans[-1] == "a":
                    b -= 1
                    ans.append("b")
                else:
                    a -= 1
                    ans.append("a")
            else:
                if a > b:
                    ans.append("a")
                    a -= 1
                else:
                    ans.append("b")
                    b -= 1

        return "".join(ans)