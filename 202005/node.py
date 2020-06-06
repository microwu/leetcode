class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        if self == None:
            return "None"
        else:
            return str(self.val)
    def show(self):
        current = self
        count = 0
        while current!=None and count < 20:
            print(current,end="->")
            current = current.next
            count+=1
        print(current)

'''
List of node
'''
class NodeList:
    def __init__(self, lists):
        self.lists = []
        for i in range(len(lists)):
            root = ListNode(lists[i][0])
            current = root
            for j in range(1,len(lists[i])):
                current.next = ListNode(lists[i][j])
                current = current.next
            self.lists.append(root)
    def __str__(self):
        _str = ""
        for node in self.lists:
            current = node
            while current != None:
                _str+=str(current)+"->"
                current = current.next
            _str+=str(current)+'\n'
        return _str
    def __getitem__(self,n):
        return self.lists[n]
    def __iter__(self):
        return (node for node in self.lists)
