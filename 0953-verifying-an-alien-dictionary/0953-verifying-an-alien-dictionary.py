class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}

        def in_order(word1, word2):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    return order_map[c1] < order_map[c2]
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False

        return True