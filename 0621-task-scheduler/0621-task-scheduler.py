from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        count_max = sum(1 for f in freq.values() if f == max_freq)

        frame = (max_freq - 1) * (n + 1) + count_max

        return max(len(tasks), frame)