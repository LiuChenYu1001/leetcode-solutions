class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tem = []

            for i in range(0, len(s), k):
                group = s[i:i + k]
                total = sum(int(num) for num in group)
                tem.append(str(total))

            s = "".join(tem)

        return s