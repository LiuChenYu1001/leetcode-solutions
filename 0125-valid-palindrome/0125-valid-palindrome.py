class Solution:
    def isPalindrome(self, s: str) -> bool:
        tem_list = []

        for ch in s:
            if "a" <= ch <= "z" or "A" <= ch <= "Z" or "0" <= ch <= "9":
                if "A" <= ch <= "Z":
                    tem_list.append(chr(ord(ch) + 32))
                else:
                    tem_list.append(ch)

        left, right = 0, len(tem_list) - 1
        while left <= right:
            if tem_list[left] != tem_list[right]:
                return False
            left += 1
            right -= 1
        
        return True