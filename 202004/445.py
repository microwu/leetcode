# add two num ii
'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
'''

# Definition for singly-linked list.
class NumList:
    def __init__(self,head = None):
        self.head = head
    def push_back(self,node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None :
                current = current.next
            current.next = node
    def get_head(self):
        return self.head
    def __str__(self):
        current = self.head
        s = ''
        while current != None:
            s += str(current.val)+'->'
            current = current.next
        s = s[0:len(s)-2]
        return s

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        current = self
        s = ''
        while current != None:
            s += '{}->'.format(current.val)
            current = current.next
        s = s[0:len(s)-2]
        return s

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = l1
        count = 0
        while current!=None:
            count += 1
            current = current.next
        current = l2
        while current!=None:
            count -= 1
            current = current.next
        if count > 0: # len1 > len2
            for _ in range(count):
                tmp = l2
                l2 = ListNode(0)
                l2.next = tmp
        elif count < 0:
            for _ in range(-count):
                tmp = l1
                l1 = ListNode(0)
                l1.next = tmp
        def addNode(n1,n2):
            if n1==None or n2==None:
                return 0
            else:
                carry = addNode(n1.next,n2.next)
                val = carry+n1.val+n2.val
                n1.val = val%10
                return val//10
        carry = addNode(l1,l2)
        if carry == 1:
            tmp = ListNode(1)
            tmp.next = l1
            return tmp
        else:
            return l1

if __name__ == "__main__":
    l1 = NumList()
    l2 = NumList()
    for i in [7,2,4,3]:
        l1.push_back(ListNode(i))
    for j in [5,2,6,4]:
        l2.push_back(ListNode(j))
    s = Solution()
    res = s.addTwoNumbers(l1.get_head(),l2.get_head())
    print(res)