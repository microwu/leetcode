class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_head = None
        self.cache_tail = None
        self.cache_map = {}

    def update_cache(self,key,val=0):
        if key in self.cache_map:
            node = self.cache_map[key]
            if node is self.cache_tail:
                pass
            elif node is self.cache_head:
                old_tail = self.cache_tail
                node.next.pre = None
                self.cache_head = node.next
                node.pre = old_tail
                node.next = None
                self.cache_tail = node
                old_tail.next = node
            else:
                node.pre.next,node.next.pre = node.next,node.pre
                self.cache_tail.next = node
                node.pre = self.cache_tail
                self.cache_tail = node
        else:
            node = ListNode(key,val)
            self.cache_map[key] = node
            if self.cache_head == None and self.capacity>0:
                self.cache_head = self.cache_tail = node
                self.capacity -= 1
            else:
                node.pre = self.cache_tail
                self.cache_tail.next = node
                self.cache_tail = node
                if self.capacity==0:
                    if self.cache_head is self.cache_tail:
                        self.cache_head = node
                        self.cache_tail = node
                    else:
                        del self.cache_map[self.cache_head.key]
                        self.cache_head.pre = None
                        self.cache_head = self.cache_head.next
                else:
                    self.capacity-=1

    def get(self, key: int) -> int:
        if key in self.cache_map:
            self.update_cache(key)
            print(self.cache_map[key].val)
            return self.cache_map[key].val
        else:
            print(-1)
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map[key].val = value
            self.update_cache(key)
        else:
            self.update_cache(key,value)



# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    cache.get(4)
    cache.get(3)
    cache.get(2)
    cache.get(1)
    cache.put(5, 5)
    cache.get(1)
    cache.get(2)
    cache.get(3)
    cache.get(4)
    cache.get(5)