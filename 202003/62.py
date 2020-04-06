class Solution:
    def __init__(self,n,m):
        self.n = n # total
        self.m = m # count
        self.lastRemaining(n,m)
    def lastRemaining(self, n: int, m: int) -> int:
        list_ = [i for i in range(n)]
        current = m-1
        while len(list_)>1:
            if current >= len(list_):
                current = current%len(list_)
            del list_[current]
            current+=m-1
        return list_[0]

if __name__ == '__main__':
    n,m = 70866,116922
    s = Solution(n,m)
