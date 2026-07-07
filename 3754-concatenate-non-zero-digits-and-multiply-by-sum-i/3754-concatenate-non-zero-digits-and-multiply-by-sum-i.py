class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = ""
        sum_of_digits = 0
        n = str(n)

        for ch in n:
            sum_of_digits += int(ch)

            if ch != "0":
                digits += ch
                
        if digits == "":
            return 0

        ans = int(digits) * sum_of_digits

        return ans