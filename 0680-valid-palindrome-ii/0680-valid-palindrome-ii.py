class Solution:
    def validPalindrome(self, s: str) -> bool:
        def find_pali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return find_pali(left + 1, right) or find_pali(left, right - 1)

            left += 1
            right -= 1

        return True 