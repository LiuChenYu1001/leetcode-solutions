class Solution:
    def isHappy(self, n: int) -> bool:
        def nxt_num(x):
            nxt = 0

            while x > 0:
                tem = x % 10
                nxt += tem * tem
                x //= 10

            return nxt 

        slow = fast = n

        while True:
            slow = nxt_num(slow)
            fast = nxt_num(nxt_num(fast))

            if fast == 1:
                return True

            if fast == slow:
                return False