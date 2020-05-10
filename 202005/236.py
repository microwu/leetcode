'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self,treeList):
        if len(treeList) == 0:
            return None
        self.root = TreeNode(treeList[0])
        def initTree(node,index):
            if node:
                node.left = index*2+1<len(treeList) and treeList[index*2+1] is not None and TreeNode(treeList[index*2+1])
                node.right = index*2+2<len(treeList) and treeList[index*2+2] is not None and TreeNode(treeList[index*2+2])
                initTree(node.left,index*2+1)
                initTree(node.right,index*2+2)
        initTree(self.root,0)
    def __str__(self):
        treeList = []
        def pot(node,treeList:List):
            if node:
                treeList.append(node.val)
                pot(node.left,treeList)
                pot(node.right,treeList)
        pot(self.root,treeList)
        return str(treeList)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,val1,val2,path):
            if node:
                path.append(node.val)
                if node.val == val1:
                    self.path1 = path[:]
                elif node.val == val2:
                    self.path2 = path[:]
                dfs(node.left,val1,val2,path)
                dfs(node.right,val1,val2,path)
                path.pop()
        path,self.path1,self.path2 = [],[],[]
        dfs(root,p,q,path)
        print(self.path1,self.path2)
        for node in self.path1:
            if node in self.path2:
                return node


if __name__ == "__main__":
    t = Tree([3,5,1,6,2,0,8,None,None,7,4])
    p = 5
    q = 1
    s = Solution()
    print(s.lowestCommonAncestor(t.root,p,q))
    # print(t)