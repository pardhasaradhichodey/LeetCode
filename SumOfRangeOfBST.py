# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def makeList(aNode):
            if aNode is None:
        # Stop recursing here
                return []
            return makeList(aNode.left) + [aNode.val] + makeList(aNode.right)
        a=makeList(root)
        res=0
        for i in a:
            if i>=low and i<=high:
                res+=i
        return res