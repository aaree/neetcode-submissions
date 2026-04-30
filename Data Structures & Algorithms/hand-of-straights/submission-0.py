class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c=Counter(hand)
        hand.sort()
        for i in hand:
            if c[i]>0:
                curr=i
                c[curr]-=1
                for j in range(groupSize-1):
                    curr+=1
                    if c[curr]<=0:
                        return False
                    c[curr]-=1
        return True