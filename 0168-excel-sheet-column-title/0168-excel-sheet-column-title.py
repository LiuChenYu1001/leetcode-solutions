class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []

        while columnNumber > 0:
            columnNumber -= 1
            tem = columnNumber % 26

            ans.append(chr(ord("A") + tem))
            columnNumber //= 26

        return "".join(reversed(ans))