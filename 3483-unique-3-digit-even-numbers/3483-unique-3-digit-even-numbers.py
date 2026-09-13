from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        ans = 0

        for a in count:
            if a == 0:
                continue
            count[a] -= 1

            for b in count:
                if count[b] == 0:
                    continue
                count[b] -= 1

                for c in count:
                    if count[c] == 0 or c % 2 != 0:
                        continue
                    ans += 1

                count[b] += 1
            count[a] += 1

        return ans