from node import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def moreThanK(node):
            count = 0
            while node:
                count+=1
                if count>=k:
                    return True
                node=node.next
            return False
        root = ListNode(None)
        pre = root
        current = head
        while moreThanK(current):
            if not current or not current.next:
                break
            current_next = current.next
            current_next_next = current.next.next
            loop_head = current
            for _ in range(k-1):
                current_next.next = current
                current, current_next = current_next,current_next_next
                if current_next_next:
                    current_next_next = current_next_next.next
            pre.next = current
            pre = loop_head
            current = current_next
        pre.next = current

        # flag = False
        return root.next

if __name__ == "__main__":
    # node_list = NodeList([[1,2,3,4,5,6,7,8]])
    node_list = NodeList([[1,2]])
    head = node_list[0]
    # head.show()
    s = Solution()
    s.reverseKGroup(head,2).show()