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
        def init(node,index):
            if index >= len(treeList) or not node:
                return None
            else:
                node.left = treeList[index*2+1] and TreeNode(treeList[index*2+1])
                init(node.left,index*2+1)
                node.right = treeList[index*2+2] and TreeNode(treeList[index*2+2])
                init(node.right,index*2+2)
        init(self.root,0)

from typing import List
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # def isValid(node):
        #     return 
        pass

if __name__ == "__main__":
    tree = Tree([5,1,4,None,None,3,6])
    root = tree.root
    s = Solution()
    s.isValidBST(root)