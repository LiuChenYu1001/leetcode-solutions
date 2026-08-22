class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def digit_sum_pro(num):
            num = str(num)
            ans1 = 0
            ans2 = 1

            for ch in num:
                ans1 += int(ch)
                ans2 *= int(ch)

            return (ans1, ans2)

        a, b = digit_sum_pro(n)
        tem = a + b

        if n % tem == 0:
            return True
        else:
            return False