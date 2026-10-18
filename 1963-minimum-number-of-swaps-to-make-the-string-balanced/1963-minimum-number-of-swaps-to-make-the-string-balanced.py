class Solution:
    def minSwaps(self, s: str) -> int:
        balance = max_balance = 0

        for c in s:
            if c == "[":
                balance += 1
            else:
                balance -= 1
            
            max_balance = max(-balance, max_balance)

        return (max_balance + 1) // 2