class Solution:
    def waysToChange(self, n: int) -> int:
        coin = [1,5,10,25]
        def dp(i,v):
            if i == 0 or v == 0:
                return 1
            elif v < 0 :
                return 0
            return dp(i-1,v)+dp(i,v-coin[i])
        return dp(3,n)

if __name__ == "__main__":
    s = Solution()
    print(s.waysToChange(5))