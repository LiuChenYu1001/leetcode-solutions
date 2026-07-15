class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = sum(range(1, 2 * n, 2))
        sumEven = sum(range(2, 2 * n + 1, 2))       

        def gcd(a, b):
            while b:
                a, b = b, a % b

            return a

        return gcd(sumOdd, sumEven)