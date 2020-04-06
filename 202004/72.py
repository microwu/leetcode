# 72.edit-distance
'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

    1.插入一个字符
    2.删除一个字符
    3.替换一个字符

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
'''

class Solution:
    def __init__(self, word1: str, word2: str):
        self.minDistance(word1,word2)
    def minDistance(self, word1: str, word2: str) -> int:
        size1 = len(word1)+1
        size2 = len(word2)+1
        answer = [[0 for _ in range(size2)] for _ in range(size1)]
        for i in range(size1):
            answer[i][0] = i
        for j in range(size2):
            answer[0][j] = j
        for i in range(1,size1):
            for j in range(1,size2):
                if word1[i-1]==word2[j-1]:
                    answer[i][j] = min(answer[i-1][j-1],answer[i-1][j]+1,answer[i][j-1]+1)
                else:
                    answer[i][j] = min(answer[i-1][j-1]+1,answer[i-1][j]+1,answer[i][j-1]+1)
        print("answer[{}][{}]:{}".format(size1-1,size2-1,answer[size1-1][size2-1]))
        print("    _   ",end="")
        for c in word2:
            print("{:<4}".format(c),end="")
        print("")
        for i in range(size1):
            if i != 0:
                print("{:<4}".format(word1[i-1]),end="")
            else:
                print("_   ",end="")
            for j in range(size2):
                print("{:<4}".format(answer[i][j]),end="")
            print("")
        return answer[size1-1][size2-1]

if __name__ == "__main__":
    word1 = "zoologicoarchaeologist"
    word2 = "zoogeologist"
    # word1 = "horse"
    # word2 = "ros"
    s = Solution(word1,word2)
