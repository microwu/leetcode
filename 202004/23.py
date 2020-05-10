from typing import List
from node import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        res = lists[0]
        for i in range(1,len(lists)):
            if res.val > lists[i].val:
                current = res
                res = lists[i]
                res_current = res
            else:
                current = lists[i]
                res_current = res
            while current!=None:
                if res_current.next == None:
                    res_current.next = current
                    break
                if current.val < res_current.next.val:
                    tmp = current.next
                    current.next = res_current.next
                    res_current.next = current
                    current = tmp
                else:
                    res_current = res_current.next
        return res

if __name__ == "__main__":
    lists = [
        [1,4,5],
        [1,3,4],
        [2,6]
    ]
    nl = NodeList(lists)
    s = Solution()
    s.mergeKLists(list(nl)).show()