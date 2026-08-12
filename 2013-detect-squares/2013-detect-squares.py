from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.point = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.freq[(x, y)] += 1
        self.point.append((x, y))

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        for nx, ny in self.point:
            if ny != y or nx == x:
                continue

            d = nx - x

            ans += self.freq[(x, y + d)] * self.freq[(nx, y + d)]
            ans += self.freq[(x, y - d)] * self.freq[(nx, y - d)]

        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)