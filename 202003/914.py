from typing import List
from collections import defaultdict
class Solution:
    def __init__(self,deck):
        print(self.hasGroupsSizeX(deck))
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        for i in set(deck):
            print(i)
        # deck_dict = defaultdict(int)
        # for num in deck:
        #     deck_dict[num]+=1
        # sorted_dict = sorted(deck_dict.items(),key=lambda item:item[1])
        # new_deck = []
        # for card in sorted_dict:
        #     new_deck.extend([card[0]]*card[1])
        # deck = new_deck
        # step=2
        # while step<=len(deck) and deck[step-1]==deck[0]:
        #     left = 0
        #     right = step-1
        #     if right == len(deck)-1:
        #         return True
        #     while right < len(deck):
        #         if deck[left] == deck[right]:
        #             left += step
        #             right += step
        #             if right == len(deck)-1:
        #                 return True
        #         else:
        #             break
        #     step+=1
        # return False

if __name__ == '__main__':
    deck = [0,0,0,0,0,1,1,2,3,4]
    s = Solution(deck)
