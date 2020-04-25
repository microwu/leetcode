class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        sub_str = {}
        next_sub = s1
        times = 0
        while True:
            i,j = 0,0
            if next_sub == "abababa":
                print(next_sub)
            while i < len(s2):
                if next_sub[j]==s2[i]:
                    i+=1
                    j+=1
                else:
                    j+=1
                if j>=len(next_sub):
                    sub_str[next_sub] = times
                    j = 0
            times += 1
            if next_sub in sub_str:
                break
        print(sub_str)
        return ""

if __name__ == "__main__":
    s1 ="acb"
    n1 = 4
    s2 ="ab"
    n2 = 2
    # s1 = "aaa"
    # n1 = 3
    # s2 = "aa"
    # n2 = 1
    s1 = "baba"
    n1 = 11
    s2 = "baab"
    n2 = 7
    s = Solution()
    print(s.getMaxRepetitions(s1,n1,s2,n2))