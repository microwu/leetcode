class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        def dp(K,N):
            if (K,N) not in memo:
                if N == 0:
                    return 0
                elif K == 1:
                    return N
                else:
                    lo,hi = 1,N
                    while lo+1 < hi:
                        f = (lo+hi) // 2
                        broken = dp(K-1,f-1)
                        intact = dp(K,N-f)
                        if broken < intact:
                            lo = f
                        elif broken > intact:
                            hi = f
                        else:
                            lo=hi=f
                    memo[K,N] = 1 + min(max(dp(K,N-f),dp(K-1,f-1)) for f in (lo,hi))
            return memo[K,N]
        return dp(K,N)
            # return 1 + min(max(self.superEggDrop(K,N-f),self.superEggDrop(K-1,f-1)) for f in range(1,N+1))

if __name__ == "__main__":
    s = Solution()
    print(s.superEggDrop(2,100))
    # for j in [2,3]:
    #     print("j:{}".format(j))
    #     for i in range(1,20):
    #         print(s.superEggDrop(j,i,i))