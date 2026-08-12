from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        queue = deque()
        queue.append("0000")
        visited = {"0000"}
        ans = 0

        while queue:
            for _ in range(len(queue)):
                tem = queue.popleft()

                if tem == target:
                    return ans

                for i in range(4):
                    digit = int(tem[i])

                    for move in [-1, 1]:
                        new_digit = (digit + move) % 10
                        nxt = tem[:i] + str(new_digit) + tem[i + 1:]

                        if nxt in deadends:
                            continue

                        if nxt in visited:
                            continue

                        visited.add(nxt)
                        queue.append(nxt)
            
            ans += 1

        return -1