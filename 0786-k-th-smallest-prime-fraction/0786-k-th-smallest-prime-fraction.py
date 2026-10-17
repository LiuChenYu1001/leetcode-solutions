class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        tem = []
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                tem.append((arr[i] / arr[j], arr[i], arr[j]))

        tem.sort()
        target, a, b  = tem[k - 1]

        return [a, b]