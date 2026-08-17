from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                need = count[card]

                for x in range(card, card + groupSize):
                    if count[x] < need:
                        return False

                    count[x] -= need

        return True