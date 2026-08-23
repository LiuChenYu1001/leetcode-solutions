class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2

        s1 = s2 = c1 = c2 = 0

        for i in range(half):
            if num[i] == "?":
                c1 += 1
            else:
                s1 += int(num[i])

        for j in range(half, len(num)):
            if num[j] == "?":
                c2 += 1
            else:
                s2 += int(num[j])

        if (c1 + c2) % 2 == 1:
            return True

        return not (s1 - s2) == 9 * (c2 - c1) // 2