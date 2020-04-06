# 460. LFU cache
'''
设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。
在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。

一个项目的使用次数就是该项目被插入后对其调用 get 和 put 函数的次数之和。使用次数会在对应项目被移除后置为 0。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
'''
import json
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.timestamp = 0

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        self.timestamp += 1
        if key in self.dict:
            value = self.dict[key][0]
            freq = self.dict[key][1]
            self.dict[key] = (value,freq+1,self.timestamp)
            return self.dict[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # print("{}:({},{},{})".format(key,value,0,self.timestamp))
        self.timestamp += 1
        if key in self.dict:
            freq = self.dict[key][1]
            self.dict[key] = (value,freq+1,self.timestamp)
        else:
            if len(self.dict) >= self.capacity:
                first = sorted(self.dict.items())[0][0]
                lf = self.dict[first][1]
                rts = self.dict[first][2]
                for key_ in self.dict:
                    if self.dict[key_][1] == lf and self.dict[key_][2] < rts:
                        first = key_
                        lf = self.dict[key_][1]
                        rts = self.dict[key_][2]
                    elif self.dict[key_][1] < lf:
                        first = key_
                        lf = self.dict[key_][1]
                        rts = self.dict[key_][2]
                del self.dict[first]
            self.dict[key] = (value,0,self.timestamp)
    
    def __str__(self):
        return json.dumps(self.dict)


# Your LFUCache object will be instantiated and called as such:
cache = LFUCache(0)
# cache.put(2, 2)
# cache.put(1, 1)
# cache.put(3, 3)
# cache.put(4, 4)
# print(cache)
# cache.get(2)
# cache.get(1)
# cache.get(2)
# cache.put(3, 3)
# print(cache)
# cache.put(4, 4)
# print(cache)
# cache.get(3)
# cache.get(2)
# cache.get(1)
# cache.get(4)
cache.put(2,1)
cache.put(2,2)
print(cache)