'''
1111. 有效括号的嵌套深度
示例 1：

输入：seq = "(()())"
输出：[0,1,1,1,1,0]
示例 2：

输入：seq = "()(())()"
输出：[0,0,0,1,1,0,1,1]
解释：本示例答案不唯一。
按此输出 A = "()()", B = "()()", max(depth(A), depth(B)) = 1，它们的深度最小。
像 [1,1,1,0,0,1,1,1]，也是正确结果，其中 A = "()()()", B = "()", max(depth(A), depth(B)) = 1 。
'''
from typing import List
import math
class Solution:
    def __init__(self,seq: str):
        self.maxDepthAfterSplit(seq)
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        answer = []
        depth,max_depth = 0,0
        for parm in seq:
            if parm == '(':
                depth+=1
                max_depth = max(depth,max_depth)
            elif parm == ')':
                depth-=1
        depth = 0
        max_depth = math.floor(max_depth/2)
        for parm in seq:
            if parm == '(':
                depth += 1
                if depth<= max_depth:
                    answer.append(0)
                else:
                    answer.append(1)
            elif parm == ')':
                if depth<= max_depth:
                    answer.append(0)
                else:
                    answer.append(1)
                depth-=1
        print(answer)


if __name__ == "__main__":
    s = Solution("(()())")
    s = Solution("()(())()")
    s = Solution("(((()))((())))")