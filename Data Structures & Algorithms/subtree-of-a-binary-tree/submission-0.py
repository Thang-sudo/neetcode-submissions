# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif (root and not subRoot) or (not root and subRoot):
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # search for a node in root tree where that node equals to subroot.val
        # if we find that node, take it as a potential subtree and compare all values with subroot to see if they all equal
        if not root and not subRoot:
            return False # Reached the end and dont find any subtree that matches subroot
        elif (not root and subRoot) or (root and not subRoot):
            return False
        elif root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        