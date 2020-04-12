# 22 括号生成
'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def insert(parentheses,s,position):
            if position == 0:
                return parentheses+s
            elif position == len(s)-1:
                return s+parentheses
            else:
                return s[0:position]+parentheses+s[position:]
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        res = set()
        res.add("()")
        step = 1
        s = "()"
        while step < n:
            new_set = set()
            for s in res:
                i = 0
                while i <= len(s):
                    new_s = insert("(",s,i)
                    j = i+1
                    while j <= len(new_s):
                        # print("new_s_i{}:{}".format(i,new_s))
                        new_set.add(insert(")",new_s,j))
                        # print("new_s_j{}:{}".format(j,insert(")",new_s,j)))
                        j+=1
                    i+=1
            step+=1
            res = new_set
            print(list(res))
        return list(res)

if __name__ == "__main__":
    n = 3
    s = Solution()
    s.generateParenthesis(n)