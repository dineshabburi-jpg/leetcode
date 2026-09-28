class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}

        for card in hand:
            count[card] = count.get(card, 0) + 1

        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]

                for i in range(card, card + groupSize):
                    if count.get(i, 0) < freq:
                        return False

                    count[i] -= freq

        return True