from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        one1 = []
        one2 = []

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    one1.append((r, c))

                if img2[r][c] == 1:
                    one2.append((r, c))

        count = defaultdict(int)
        ans = 0

        for r1, c1 in one1:
            for r2, c2 in one2:
                dr = r1 - r2
                dc = c1 - c2
                
                count[(dr, dc)] += 1
                ans = max(ans, count[(dr, dc)])

        return ans