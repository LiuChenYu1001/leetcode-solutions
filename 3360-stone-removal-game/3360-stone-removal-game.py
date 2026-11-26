class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_win = False
        tem = 10

        while n >= tem:
            n -= tem
            alice_win = not alice_win
            tem -= 1

        return alice_win