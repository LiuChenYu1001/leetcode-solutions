class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, left, right):
            if left == 0 and right == 0:
                ans.append(path)
                return

            if left > 0:
                backtrack(path + "(", left - 1, right)

            if right > left:
                backtrack(path + ")", left, right - 1)

        backtrack("", n, n)

        return ans