# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = l1
        while l1 is None and l2 is None:
            if l1 and l2:
                l1.val = l1.val+l2.val
            if l1>=10:
                if l1.next == None:
                    l1.next = ListNode(1)
                else:
                    l1.next.val+=1
            elif l1.next == None and l2.next != None:
                l1.next = ListNode(0)
            if l2 != None:
                l2 = l2.next
            l1 = l1.next
        return root


