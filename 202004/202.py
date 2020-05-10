from functools import reduce
class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()
        res.add(n)
        while True:
            if n == 1:
                return True
            else:
                n = list(str(n))
                n = reduce(lambda x,y:x+int(y)**2,n,0)
                if n in res:
                    return False
        
if __name__ == "__main__":
    n = 2
    s = Solution()
    print(s.isHappy(n))
