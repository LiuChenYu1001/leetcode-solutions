from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        words = list(freq.keys())
        words.sort(key = lambda x: (-freq[x], x))

        return words[:k]