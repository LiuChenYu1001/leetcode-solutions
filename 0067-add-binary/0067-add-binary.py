class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            cur = carry

            if i >= 0:
                cur += int(a[i])
                i -= 1

            if j >= 0:
                cur += int(b[j])
                j -= 1

            ans.append(str(cur % 2))
            carry = cur // 2

        return "".join(ans[::-1])